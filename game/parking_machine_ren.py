"""renpy
init python:
"""

# from datetime import datetime
from enum import Enum
from typing import Optional

import pygame
from renpy import config
from renpy.display.imagelike import Solid

# TODO change game cursor to tweezers (img on Desktop)


class EMWW_GameDifficulty(Enum):
    MWWGD_Easy = .2
    MWWGD_Normal = .4
    MWWGD_Nightmare = .8


class DynamicLogicSimple:
    def __init__(self, *args) -> None:
        self.m_barPos = 0
        self.m_pointerPos = 0
        self.m_barInteriaTimer = 0
        self.m_lastInHotspot = True
        self.m_tiredFactor = 0
        self.m_barSpeed = .1

    def UpdateInput(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.SetPointerPos(self.m_pointerPos + value * .02)

    def GetBarPos(self) -> float:
        return self.m_barPos

    def GetPointerPos(self) -> float:
        return self.m_pointerPos

    def UpdateLogic(self, isPointerInHotSpot: bool, timeDelta: float) -> bool:
        return self.ProcessLogic(isPointerInHotSpot, timeDelta)

    def GetWinner(self) -> bool:
        return self.m_winner

    def GetBarWidthScale(self) -> float:
        return max(1 - self.m_tiredFactor, .3)

    def SetPointerPos(self, pos: float) -> None:
        pos = min(pos, 1)
        pos = max(pos, -1)
        self.m_pointerPos = pos

    def ProcessLogic(self, isPointerInHotSpot: bool, timeDelta: float) -> bool:
        if isPointerInHotSpot:
            if self.m_barInteriaTimer > 0:
                self.m_barInteriaTimer -= timeDelta
                self.m_barPos -= timeDelta * self.m_barSpeed
            else:
                self.m_barPos += timeDelta * self.m_barSpeed
            self.m_lastInHotspot = True
        else:
            if self.m_lastInHotspot:
                self.m_barInteriaTimer = 1
            self.m_barPos -= timeDelta * self.m_barSpeed
            self.m_lastInHotspot = False

        if self.m_tiredFactor < 1:
            self.m_tiredFactor += timeDelta * .03

        if self.m_tiredFactor > .5:
            self.m_barSpeed += timeDelta * .01
            self.m_barSpeed = min(self.m_barSpeed, .5)

        if self.m_barPos >= .9:
            self.m_winner = True
            return True
        elif self.m_barPos < -.9:
            self.m_winner = False
            return True

        return False


class DynamicLogicSimpleCont(DynamicLogicSimple):
    def __init__(self, *args) -> None:
        super().__init__(args)
        self.m_barShift = 0

    def UpdateInput(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.m_barShift = value * .03
        self.SetPointerPos(self.m_pointerPos + value * .02)

    def UpdateLogic(self, isPointerInHotSpot: bool, timeDelta: float) -> bool:
        self.SetPointerPos(self.m_pointerPos + self.m_barShift)
        return self.ProcessLogic(isPointerInHotSpot, timeDelta)


class DynamicLogicNewton(DynamicLogicSimple):
    def __init__(self, difficulty: EMWW_GameDifficulty):
        super().__init__()
        # lengths of vectors
        self.m_barVelocity = 0
        self.m_barAcceleration = 0

        self.m_barMass = .5
        self.m_distractingForce = 0
        self.m_distractingForceCurr = 0
        self.m_distractingForceTimer = 0
        self.ApplyDifficultySettings(difficulty)

    def UpdateInput(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.m_barAcceleration = value / (self.m_barMass * 6)

    def UpdateLogic(self, isPointerInHotSpot: bool, timeDelta: float) -> bool:
        self.m_distractingForceTimer -= timeDelta
        if self.m_distractingForceTimer <= 0:
            self.m_distractingForce = -self.m_distractingForce
            self.m_distractingForceTimer = 0.3
            self.m_distractingForceCurr = self.m_distractingForce

        self.m_barVelocity += self.m_distractingForceCurr * timeDelta

        self.m_barVelocity += self.m_barAcceleration * timeDelta

        self.m_barVelocity = min(self.m_barVelocity, 1)
        self.m_barVelocity = max(self.m_barVelocity, -1)

        self.SetPointerPos(self.m_pointerPos + (self.m_barVelocity * timeDelta))
        return self.ProcessLogic(isPointerInHotSpot, timeDelta)

    def ApplyDifficultySettings(self, difficulty: EMWW_GameDifficulty) -> None:
        # we could also change the m_barMass
        self.m_distractingForce = difficulty.value


class DynamicLogicMash(DynamicLogicSimple):
    def __init__(self, *args) -> None:
        super().__init__()
        self.m_barVelocity = 0
        self.m_barAcceleration = 0
        self.m_barMass = 2

    def UpdateInput(self, value: float) -> None:
        value = abs(value)
        if value > .001:
            self.m_barAcceleration = value / (self.m_barMass * 2)

    def UpdateLogic(self, isPointerInHotSpot: bool, timeDelta: float) -> bool:
        fraction = .8 if self.m_barVelocity > 0 else .5
        self.m_barAcceleration -= timeDelta * fraction

        # maximum acceleration
        if self.m_barVelocity > 0 and self.m_barAcceleration < -3:
            self.m_barAcceleration = -3
        elif self.m_barVelocity <= 0 and self.m_barAcceleration < -2.5:
            self.m_barAcceleration = -2.5
        elif self.m_barVelocity > 0 and self.m_barAcceleration > 1.2:
            self.m_barAcceleration = 1.2
        elif self.m_barVelocity <= 0 and self.m_barAcceleration > 2:
            self.m_barAcceleration = 2.0

        self.m_barVelocity += self.m_barAcceleration * timeDelta

        # maximum velocity
        self.m_barVelocity = min(self.m_barVelocity, .2)
        self.m_barVelocity = max(self.m_barVelocity, -.3)

        self.SetPointerPos(self.m_pointerPos + (self.m_barVelocity * timeDelta))
        result = self.ProcessLogic(isPointerInHotSpot, timeDelta)

        print('WristWrestling', f"Acceleration : {self.m_barAcceleration}")
        print('WristWrestling', f"Velocity : {self.m_barVelocity}")

        return result


class ParkingDisplayable(renpy.display.displayable.Displayable):
    def __init__(self, logic: DynamicLogicSimple) -> None:
        super().__init__()

        self.has_ended = False
        self.success = False
        self.logic = logic
        self.bar_width = 200  # TODO
        self.bar_drawable = Solid(
            '#ff8000', xsize=self.bar_width, ysize=50,
        )
        # self.cur_y = 700
        self.cur_y = renpy.game.preferences.physical_size[1] * .85 - 10
        self.bar_y = config.screen_height * .85 - 43
        # pygame.mouse.set_pos([700, self.cur_y])  # somehow relative, but config.screen_height is not working
        self.screen_width_half = renpy.game.preferences.physical_size[0] // 2
        self.bulgar_const = renpy.game.preferences.physical_size[0] / config.screen_width
        self.pos_min = self.screen_width_half - self.screen_width_half // 3
        # self.pos_max = self.screen_width_half + 250
        self.pos_x = self.screen_width_half
        pygame.mouse.set_pos([self.pos_x, self.cur_y])
        # record all the drawables for self.visit
        self.drawables = [
            self.bar_drawable,
        ]
        # time = renpy.get_time()
        self.start_time = 0

    def render(self, width: int, height: int, st: float, *_) -> renpy.Render:
        """
        Called to display this displayable. This is called with width
        and height parameters, which give the largest width and height
        that this drawable can be drawn to without overflowing some
        bounding box. It's also given two times. It returns a Surface
        that is the current image of this drawable.

        @param st: The time since this widget was first shown, in seconds.
        @param at: The time since a similarly named widget was first shown, in seconds.
        """
        render = renpy.Render(width, height)

        if not self.start_time:
            self.start_time = st

        xsize = int(self.logic.GetBarWidthScale() * self.bar_width)
        print('xsize', xsize)
        x_place = self.logic.GetBarPos() * 250 + (config.screen_width - xsize) / 2  # center

        self.bar_drawable = Solid(
            '#ff8000', xsize=xsize, ysize=50,
        )
        self.bar_drawable.xsize = xsize
        self.bar_drawable.x_place = x_place  # pylint: disable attribut outside init

        render.place(
            self.bar_drawable,
             # scale to (-250 to 250)
            x=x_place, y=self.bar_y,
        )

        # find out if the cursor is inside hotspot
        # this should probably be managable by the pygame's collisions
        inside_hotspot = self.bar_drawable.x_place - self.bar_drawable.xsize <= self.pos_x / self.bulgar_const <= self.bar_drawable.x_place + self.bar_drawable.xsize
        seconds = st - self.start_time
        if seconds >= 0.1:
            self.start_time = st
            end = self.logic.UpdateLogic(inside_hotspot, seconds)
            if end:
                self.has_ended = True
        self.set_pointer_pos()

        renpy.redraw(self, 0)
        return render

    def set_pointer_pos(self):
        pos_x = self.logic.GetPointerPos()  # -1 to 1
        # scale to (-250 to 250) + pos_min
        self.pos_x = int((pos_x + 1) * self.screen_width_half / 3) + self.pos_min
        pygame.mouse.set_pos([self.pos_x, self.cur_y])

    def event(self, ev: pygame.event, _: float, __: float, st: float) -> Optional[bool]:
        """
        Called to report than an event has occured. Ev is the raw
        pygame event object representing that event. If the event
        involves the mouse, x and y are the translation of the event
        into the coordinates of this displayable. st is the time this
        widget has been shown for.

        @returns A value that should be returned from Interact, or None if
        no value is appropriate.
        """
        if self.has_ended:
            # refresh the screen
            renpy.restart_interaction()
            return self.logic.m_winner

        if ev.type != pygame.MOUSEMOTION:
            return

        self.logic.UpdateInput(ev.rel[0])
        self.set_pointer_pos()

        renpy.restart_interaction()
        # # find out if the cursor is inside hotspot
        # # this should probably be managable by the pygame's collisions
        # inside_hotspot = self.bar_drawable.x_place - self.bar_drawable.xsize <= pos_x <= self.bar_drawable.x_place + self.bar_drawable.xsize
        # seconds = st - self.start_time
        # if seconds >= 0.1:
        #     self.start_time = st
        #     self.logic.UpdateLogic(inside_hotspot, seconds)
        #     renpy.restart_interaction()

        #     print('updating logic', st)

        # print(ev.pos, ev.rel)
        # renpy.restart_interaction()
        # renpy.redraw(self, 0)

    def visit(self) -> list[renpy.display.displayable.Displayable]:
        """
        Called to ask the displayable to return a list of its children
        (including children taken from styles). For convenience, this
        list may also include None values.
        """
        return self.drawables
