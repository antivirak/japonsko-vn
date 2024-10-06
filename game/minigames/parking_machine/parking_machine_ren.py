"""renpy
init python:
"""

from enum import Enum
from typing import Optional

import pygame
from renpy import config, game
from renpy.display.imagelike import Solid


class GameDifficulty(Enum):
    EASY = .2
    NORMAL = .4
    HARD = .8


class DynamicLogicSimple:
    def __init__(self, *_) -> None:
        self.bar_position = .0
        self.mouse_pointer_position = .0
        self.bar_interia_timer = .0
        self.was_in_hotspot = True
        self.tired_factor = .0
        self.bar_speed = .1
        self.winner = False

    def update_input(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.pointer_position = self.mouse_pointer_position + value * .02

    def update_logic(self, pointer_in_hotspot: bool, time_delta: float) -> bool:
        return self.process_logic(pointer_in_hotspot, time_delta)

    @property
    def bar_width_scale(self) -> float:
        return max(1 - self.tired_factor, .3)

    @property
    def pointer_position(self) -> float:
        return self.mouse_pointer_position

    @pointer_position.setter
    def pointer_position(self, pos: float) -> None:
        pos = min(pos, 1)
        pos = max(pos, -1)
        self.mouse_pointer_position = pos

    def process_logic(self, pointer_in_hotspot: bool, time_delta: float) -> bool:
        if pointer_in_hotspot:
            if self.bar_interia_timer > 0:
                self.bar_interia_timer -= time_delta
                self.bar_position -= time_delta * self.bar_speed
            else:
                self.bar_position += time_delta * self.bar_speed
            self.was_in_hotspot = True
        else:
            if self.was_in_hotspot:
                self.bar_interia_timer = 1
            self.bar_position -= time_delta * self.bar_speed
            self.was_in_hotspot = False

        if self.tired_factor < 1:
            self.tired_factor += time_delta * .03

        if self.tired_factor > .5:
            self.bar_speed += time_delta * .01
            self.bar_speed = min(self.bar_speed, .5)

        if self.bar_position >= .98:
            self.winner = True
            return True
        return self.bar_position < -.9


class DynamicLogicSimpleCont(DynamicLogicSimple):
    def __init__(self, *args) -> None:
        super().__init__(args)
        self.bar_shift = .0

    def update_input(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.bar_shift = value * .03
        self.pointer_position = self.mouse_pointer_position + value * .02

    def update_logic(self, pointer_in_hotspot: bool, time_delta: float) -> bool:
        self.pointer_position = self.mouse_pointer_position + self.bar_shift
        return self.process_logic(pointer_in_hotspot, time_delta)


class DynamicLogicNewton(DynamicLogicSimple):
    def __init__(self, difficulty: GameDifficulty):
        super().__init__()
        # lengths of vectors
        self.bar_velocity = .0
        self.bar_acceleration = .0

        self.bar_mass = .5
        self.distracting_force_curr = .0
        self.distracting_force_timer = .0
        # we could also change the bar_mass
        self.distracting_force = difficulty.value

    def update_input(self, value: float) -> None:
        value = min(value, 1)
        value = max(value, -1)

        self.bar_acceleration = value / (self.bar_mass * 6)

    def update_logic(self, pointer_in_hotspot: bool, time_delta: float) -> bool:
        self.distracting_force_timer -= time_delta
        if self.distracting_force_timer <= 0:
            self.distracting_force = -self.distracting_force
            self.distracting_force_timer = 0.3
            self.distracting_force_curr = self.distracting_force

        self.bar_velocity += self.distracting_force_curr * time_delta

        self.bar_velocity += self.bar_acceleration * time_delta

        self.bar_velocity = min(self.bar_velocity, 1)
        self.bar_velocity = max(self.bar_velocity, -1)

        self.pointer_position = self.mouse_pointer_position + self.bar_velocity * time_delta
        return self.process_logic(pointer_in_hotspot, time_delta)


class DynamicLogicMash(DynamicLogicSimple):
    def __init__(self, *_) -> None:
        super().__init__()
        self.bar_velocity = .0
        self.bar_acceleration = .0
        self.bar_mass = 2

    def update_input(self, value: float) -> None:
        if abs(value) > .001:
            self.bar_acceleration = value / (self.bar_mass * 2)

    def update_logic(self, pointer_in_hotspot: bool, time_delta: float) -> bool:
        fraction = .8 if self.bar_velocity > 0 else .5
        self.bar_acceleration -= time_delta * fraction

        # maximum acceleration
        if self.bar_velocity > 0 and self.bar_acceleration < -3:
            self.bar_acceleration = -3
        elif self.bar_velocity <= 0 and self.bar_acceleration < -2.5:
            self.bar_acceleration = -2.5
        elif self.bar_velocity > 0 and self.bar_acceleration > 1.2:
            self.bar_acceleration = 1.2
        elif self.bar_velocity <= 0 and self.bar_acceleration > 2:
            self.bar_acceleration = 2.0

        self.bar_velocity += self.bar_acceleration * time_delta

        # maximum velocity
        self.bar_velocity = min(self.bar_velocity, .2)
        self.bar_velocity = max(self.bar_velocity, -.3)

        self.pointer_position = self.mouse_pointer_position + self.bar_velocity * time_delta
        return self.process_logic(pointer_in_hotspot, time_delta)


class ParkingDisplayable(renpy.display.displayable.Displayable):
    def __init__(self, logic: DynamicLogicSimple) -> None:
        super().__init__()

        self.has_ended = False
        self.success = False
        self.logic = logic
        self.bar_width = 150  # can be scaled
        self.bill_width = 500
        self.bar_drawable = Solid(
            '#ff8000', xsize=self.bar_width, ysize=50,
        )
        self.bill_drawable = Solid(  # this one is dummy
            '#ff8000', xsize=self.bar_width, ysize=50,
        )
        y_scale = .63
        self.bulgar_const = game.preferences.physical_size[0] / config.screen_width
        print(self.bulgar_const)
        self.screen_width_half = game.preferences.physical_size[0] // 2
        if game.preferences.fullscreen:
            self.cur_y = config.screen_height ** 2 / 1080 * y_scale - 20 * config.screen_height / 1080
            self.bar_y = config.screen_height * y_scale - 43 * config.screen_height / 1080
            init_pos = config.screen_width // 2
            self.pos_min = int((init_pos - init_pos / 3) / 3 * 2)
        else:
            self.cur_y = game.preferences.physical_size[1] ** 2 / 807 * y_scale - 20 * game.preferences.physical_size[1] / 807
            # config.screen_height * y_scale - 43
            self.bar_y = game.preferences.physical_size[1] / 807 * 1080 * y_scale - 43 * game.preferences.physical_size[1] / 807
            init_pos = game.preferences.physical_size[0] // 2
            self.pos_min = self.screen_width_half - self.screen_width_half // 3

        self.pos_x = init_pos
        self.x = self.pos_x
        pygame.mouse.set_pos([self.pos_x, self.cur_y])
        # record all the drawables for self.visit
        self.drawables = [
            self.bar_drawable,
            self.bill_drawable,
        ]
        # time = renpy.get_time()
        self.start_time = .0

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

        xsize = int(self.logic.bar_width_scale * self.bar_width)
        # scale to (-250 to 250)
        x_place = self.logic.bar_position * 250 + (config.screen_width - xsize) / 2  # center

        bill_size_y = 263
        self.bar_drawable = Solid(
            '#ff800090', xsize=xsize, ysize=bill_size_y,
        )

        self.bill_drawable = Crop(
            (
                int(self.bill_width - (self.logic.bar_position + 1) * 250), 0,
                self.bill_width * self.bulgar_const, bill_size_y,
            ),
            Image('images/2kyen.png'),
        )
        self.bar_drawable.xsize = xsize
        self.bar_drawable.x_place = x_place

        render.place(
            self.bill_drawable,
            x=config.screen_width / 2 - 250, y=self.bar_y,
        )
        render.place(
            self.bar_drawable,
            x=x_place, y=self.bar_y,
        )

        # find out if the cursor is inside hotspot
        # this could probably be managable by the pygame's collisions
        inside_hotspot = (
            self.bar_drawable.x_place
            <= self.x
            <= self.bar_drawable.x_place + self.bar_drawable.xsize
        )
        seconds = st - self.start_time
        if seconds >= .1:
            self.start_time = st
            end = self.logic.update_logic(inside_hotspot, seconds)
            if end:
                self.has_ended = True
        self.move_mouse()

        renpy.redraw(self, 0)
        return render

    def move_mouse(self) -> None:
        pos_x = self.logic.mouse_pointer_position  # -1 to 1
        # scale to (-250 to 250) + pos_min
        screen_width_half = config.screen_width // 2 if game.preferences.fullscreen else self.screen_width_half
        self.pos_x = int((pos_x + 1) * screen_width_half / 3 + self.pos_min)
        pygame.mouse.set_pos([self.pos_x, self.cur_y])

    def event(self, ev: pygame.event, x: float, *_: float) -> Optional[bool]:
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
            return self.logic.winner

        if ev.type != pygame.MOUSEMOTION:
            return None
        self.x = x

        self.logic.update_input(ev.rel[0])
        self.move_mouse()

        renpy.restart_interaction()
        return None

    def visit(self) -> list[renpy.display.displayable.Displayable]:
        """
        Called to ask the displayable to return a list of its children
        (including children taken from styles). For convenience, this
        list may also include None values.
        """
        return self.drawables
