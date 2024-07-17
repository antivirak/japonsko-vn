# start minigame by "jump / call parking_machine_game_main" from script


screen parking_machine_game(game_displayable):

    # disable the mous buttons for actions other than the game
    key 'mousedown_1' action NullAction()
    key 'mousedown_3' action NullAction()

    $ xsize = int(renpy.game.preferences.physical_size[0] / 3 * renpy.config.screen_width / renpy.game.preferences.physical_size[0])  # * 1.35
    add Solid("#cd2e2e", xsize=xsize, ysize=50, xalign=.5, yalign=.85)
    add game_displayable

    vbox:
        xpos 50
        ypos 50
        spacing 20

        # TODO this probably will be deleted, as we do not allow to move mouse higher than the bar
        textbutton 'Hlavní menu':
            text_hover_color '#fff'
            action [Confirm(
                'Opravdu chcete odejít do hlavního menu?',
                yes=[
                    Return(False),
                ],
            )]

    if game_displayable.has_ended:
        timer .1 action Return(game_displayable.success)


# label parking_machine_game_main:
label start:
    "Zasekla se ti bakovka v automatu na placení!"
    image black = "#000"
    scene black
    # show bg image
    $ game_displayable = ParkingDisplayable(DynamicLogicMash(EMWW_GameDifficulty.MWWGD_Easy))
    # avoid rolling back and losing game state
    $ renpy.block_rollback()

    $ success = renpy.call_screen(
        _screen_name='parking_machine_game', game_displayable=game_displayable,
    )
    $ renpy.checkpoint()
    if success is True:
        "Bankovka úspěšně vyndána z automatu!"
    else:
        "Bohužel, nepovelo se ti vyndat bankovku z automatu, takže přicházíš o 2000 jenů. Stále však šlo zaplatit mincemi."
