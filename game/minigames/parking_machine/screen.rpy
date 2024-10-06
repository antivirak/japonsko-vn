# start minigame by "jump / call parking_machine_game_main" from script

image mouse tweezers:
    "images/tweezers.png"


screen parking_machine_game(game_displayable):
    # disable the mouse buttons for actions other than the game
    key 'mousedown_1' action NullAction()
    key 'mousedown_3' action NullAction()

    $ xsize = int(renpy.game.preferences.physical_size[0] / 3 * renpy.config.screen_width / renpy.game.preferences.physical_size[0])  # * 1.35
    # add Solid("#000", xsize=xsize, ysize=10, xalign=.5, yalign=.63)
    add game_displayable

    if game_displayable.has_ended:
        timer .1 action Return(game_displayable.success)


label parking_machine_game_main:
    "Zasekla se ti bakovka v automatu na placení! Opatrně ji vytáhni pinzetou za oranžovou část."
    scene automat:
        xzoom 1.5 yzoom 1.5
    $ mouse_backup = config.mouse_displayable
    $ config.mouse_displayable = MouseDisplayable(
        "images/tweezers.png", 0, 0,
    ).add("tweezers", "mouse tweezers", 9.9, 9.9)  # Transform(, xysize=(100, 50))
    $ game_displayable = ParkingDisplayable(DynamicLogicNewton(GameDifficulty.HARD))
    # avoid rolling back and losing game state
    $ renpy.block_rollback()

    $ success = renpy.call_screen(
        _screen_name='parking_machine_game', game_displayable=game_displayable,
    )
    $ renpy.checkpoint()
    $ config.mouse_displayable = mouse_backup
    if success:
        show 2kyen:
            yalign .63
            xalign .5
        "Bankovka úspěšně vyndána z automatu!"
    else:
        menu:
            "Chceš to zkusit znovu?"
            "Ano.":
                jump parking_machine_game_main
            "Ne.":
                "Bohužel, nepovelo se ti vyndat bankovku z automatu, takže přicházíš o 2000 jenů. Stále však šlo zaplatit mincemi."
