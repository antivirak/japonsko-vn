"""renpy
init python:
"""

import pygame
from renpy import config
from renpy.display.imagelike import Solid


class ParkingDisplayable(renpy.display.displayable.Displayable):
    def __init__(self) -> None:
        super().__init__()

        self.has_ended = False
        self.success = False
        # record all the drawables for self.visit
        self.drawables = [
        ]

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

        # render.place(
        #     self.drum_bar_drawable,
        #     x=0, y=config.screen_height // 2 - self.horizontal_bar_height // 2,
        # )

        renpy.redraw(self, 0)
        return render

    def event(self, ev: pygame.event, _: float, __: float, st: float) -> None:
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
            return

        # check if some keys have been pressed
        if ev.type == pygame.MOUSEBUTTONDOWN:  # TODO do we want mousedown and hold or only move?
            drum_idx = self.button_map.get(ev.button)
        else:
            return

    def visit(self) -> list[renpy.display.displayable.Displayable]:
        """
        Called to ask the displayable to return a list of its children
        (including children taken from styles). For convenience, this
        list may also include None values.
        """
        return self.drawables
