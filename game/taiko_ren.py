"""renpy
init python:
"""

import pygame
from renpy import config
from renpy.display.imagelike import Solid

CHANNEL_NAME = 'music'  # renpy's default - volume from preferences


class RhythmGameDisplayable(renpy.display.displayable.Displayable):
    SCORE_GOOD = 60
    SCORE_PERFECT = 100

    def __init__(self) -> None:
        super().__init__()

        self.channel_name = CHANNEL_NAME

        self.has_game_started = False
        self.has_ended = False
        self.time_offset = None
        self.button_map = {1: 1, 3: 0}
        self.keycode_to_drum_idx = {
            pygame.K_x: 1,
            pygame.K_c: 0
        }

        self.drum_bar_width = int(config.screen_width * 0.85)
        self.horizontal_bar_height = 8

        self.note_width = 50

        # time between the note travels through the screen
        self.note_offset = 3.0
        # speed = distance / time
        self.note_speed = self.drum_bar_width / self.note_offset  # config.screen_width / self.note_offset

        # number of drum bars
        self.num_drum_bars = 2

        # assign notes to drums, same length as self.onset_times
        # renpy.random.randint is upper-inclusive
        self.onset_times, self.drum_idxs = self.read_beatmap()
        self.max_score = len(self.onset_times) * self.SCORE_PERFECT

        # map drum_idx to a list of active note timestamps
        self.active_notes_per_drum = {
            drum_idx: [] for drum_idx in range(self.num_drum_bars)
        }

        # map onset timestamp to whether it has been hit; initialized to False
        self.onset_hits = {
            onset: None for onset in self.onset_times
        }
        self.score = 0
        # if the note is hit within 0.3 seconds of its actual onset time
        # we consider it a hit
        # can set different threshold for Good, Great hit scoring
        # miss if you hit the note too early, 0.1 second window before note becomes hittable
        self.prehit_miss_threshold = 0.4  # seconds
        self.hit_threshold = 0.3  # seconds
        self.perfect_threshold = 0.1  # seconds
        # therefore good is btw/ hit and perfect

        # define the drawables
        self.drum_bar_drawable = Solid(
            '#fff', xsize=config.screen_width, ysize=self.horizontal_bar_height,
        )
        self.vertical_bar_drawable = Solid('#fff', xsize=8, ysize=config.screen_height)
        # map drum_idx to the note drawable
        self.note_drawables = {
            0: Solid('#3310e2', xsize=self.note_width, ysize=self.note_width),
            1: Solid('#f00', xsize=self.note_width, ysize=self.note_width),
        }

        # record all the drawables for self.visit
        self.drawables = [
            self.drum_bar_drawable,
            self.vertical_bar_drawable,
            *self.note_drawables.values(),
        ]
        self.hit_sound = {
            0: "audio/stop-deep.mp3",
            1: "audio/stop-13692.mp3",
        }

        # silence before the music plays
        silence_offset_start = 1.5  # sec
        silence_start = f'<silence {silence_offset_start}>'
        # start playing music
        renpy.music.queue([
            silence_start,
            f"<to {self.onset_times[-1] + 2}>audio/Japanese_Taiko_mp3_1710913652.mp3",
        ], channel=self.channel_name, loop=False)
        self.has_game_started = True

    @staticmethod
    def read_beatmap() -> tuple[list[float], list[float]]:
        with renpy.file('audio/beatmap.tsv', 'utf-8') as f:
            beatmap = [map(float, line.strip().split()) for line in f.readlines()]
        return tuple(zip(*beatmap))

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
        # cache the first st, when this displayable is first shown on the screen
        # this allows us to compute subsequent times when the notes should appear
        if self.has_game_started and self.time_offset is None:
            self.time_offset = st + self.note_offset

        render = renpy.Render(width, height)

        render.place(
            self.drum_bar_drawable,
            x=0, y=config.screen_height // 2 - self.horizontal_bar_height // 2,
        )
        render.place(
            self.vertical_bar_drawable,
            x=config.screen_width - self.drum_bar_width, y=0,
        )

        if not self.has_game_started:
            return render

        # check if the song has ended
        if renpy.music.get_playing(channel=self.channel_name) is None:
            self.has_ended = True
            renpy.timeout(0)  # raise an event
            return render

        # update self.active_notes_per_drum
        self.active_notes_per_drum = self.get_active_notes_per_drum(st)

        # render notes for each drum
        for drum_idx, note_timestamps in self.active_notes_per_drum.items():
            # loop through active notes
            for onset, note_timestamp in note_timestamps:
                # render the notes that are active and haven't been hit
                if self.onset_hits[onset] is not None:
                    continue

                note_drawable = self.note_drawables[drum_idx]

                # compute where on the vertical axes the note is
                # the vertical distance from the right that the note has already traveled
                # is given by time * speed
                note_distance_from_left = note_timestamp * self.note_speed
                x_offset = config.screen_width - self.drum_bar_width + note_distance_from_left
                render.place(
                    note_drawable,
                    x=x_offset, y=config.screen_height // 2 - self.note_width // 2,
                )

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

        if not self.has_game_started or self.time_offset is None:
            # no need to process the event
            return

        # check if some keys have been pressed
        if ev.type == pygame.MOUSEBUTTONDOWN:
            drum_idx = self.button_map.get(ev.button)
        elif ev.type == pygame.KEYDOWN:
            if ev.key not in self.keycode_to_drum_idx:
                return
            drum_idx = self.keycode_to_drum_idx[ev.key]
        else:
            return

        # look up the drum that correponds to the key pressed
        if drum_idx is None:
            return

        active_notes_on_drum = self.active_notes_per_drum[drum_idx]
        curr_time = st - self.time_offset

        # loop over active notes to check if one is hit
        for onset, _ in active_notes_on_drum:
            if self.onset_hits[onset] is not None:  # status already determined
                continue

            # compute the time difference between when the key is pressed
            # and when we consider the note hittable as defined by self.hit_threshold
            time_delta = curr_time - onset

            # perfect
            if -self.perfect_threshold <= time_delta <= self.perfect_threshold:
                self.onset_hits[onset] = 'perfect'
                self.score += self.SCORE_PERFECT
                # refresh the screen
                renpy.restart_interaction()
                break

            # good
            if (
                (-self.hit_threshold <= time_delta < self.perfect_threshold)
                or (self.perfect_threshold < time_delta <= self.hit_threshold)  # noqa: W503
            ):
                self.onset_hits[onset] = 'good'
                self.score += self.SCORE_GOOD
                renpy.restart_interaction()
                break

            # miss
            if -self.prehit_miss_threshold <= time_delta < -self.hit_threshold:
                self.onset_hits[onset] = 'miss'
                # no change to score
                renpy.restart_interaction()
                return

        renpy.play(self.hit_sound[drum_idx])

    def visit(self) -> list[renpy.display.displayable.Displayable]:
        """
        Called to ask the displayable to return a list of its children
        (including children taken from styles). For convenience, this
        list may also include None values.
        """
        return self.drawables

    def get_active_notes_per_drum(self, current_time: float) -> dict:
        active_notes = {
            drum_idx: [] for drum_idx in range(self.num_drum_bars)
        }

        for onset, drum_idx in zip(self.onset_times, self.drum_idxs):
            # determine if this note should appear on the drum
            time_before_appearance = onset - current_time + self.note_offset
            if time_before_appearance < 0:  # already below the bottom of the screen
                continue
            # should be on screen
            if time_before_appearance <= self.note_offset:
                active_notes[drum_idx].append((onset, time_before_appearance))
            # there is still time before the next note should show
            # break out of the loop so we don't process subsequent notes that are even later
            elif time_before_appearance > self.note_offset:
                break

        return active_notes
