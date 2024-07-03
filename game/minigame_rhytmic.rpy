# start minigame by "jump rhytm_game_main" from script


screen rhythm_game(rhythm_game_displayable):

    zorder 100  # always on top, covering textbox, quick_menu

    # disable the mous buttons for actions other than drumming
    key 'mousedown_1' action NullAction()
    key 'mousedown_3' action NullAction()

    add Solid("#000", xsize=.15 * config.screen_width, ysize=150, xalign=1, yalign=.5)
    add rhythm_game_displayable

    vbox:
        xpos 50
        ypos 50
        spacing 20

        textbutton 'Hlavní menu':
            text_hover_color '#fff'
            action [Confirm(
                'Opravdu chcete odejít do hlavního menu?',
                yes=[
                    Stop(CHANNEL_NAME),  # stop the music on this channel
                    Return(rhythm_game_displayable.score),
                ],
            )]

        showif rhythm_game_displayable.has_game_started:
            text 'Score:\n' + str(rhythm_game_displayable.score):
                color '#fff'
                size 40

    # return the number of hits and total number of notes to the main game
    if rhythm_game_displayable.has_ended:
        # timer 2.0 action Return(...)
        timer .1 action Return(rhythm_game_displayable.score)


# label rhytm_game_main:
label start:
    # TODO stop current music and then start again
    "Hraješ proti Mimoňovi v rytmické hře! Hraješ na bubínek."
    "Červené noty znamenají, že máš stisknout klávesu Y nebo levé tlačítko myši; modré noty znamenají, že máš stisknout klávesu X nebo pravé myšítko."
    "Klávesy se snaž stisknout až dojedou na levou stranu obrazovky. Hodně štěstí!"
    image black = "#000"
    scene black
    show taiko at topright
    $ rhythm_game_displayable = RhythmGameDisplayable()
    # avoid rolling back and losing game state
    $ renpy.block_rollback()

    # $ _game_menu_screen = None

    # show screen _performance at right
    $ new_score = renpy.call_screen(
        _screen_name='rhythm_game', rhythm_game_displayable=rhythm_game_displayable,
    )
    $ renpy.checkpoint()
    $ score = str(100 * new_score / rhythm_game_displayable.max_score)
    $ score = score[:min(5, len(score))]
    "Hra skončila! Tvoje skóre je: [new_score]; [score] procent."
