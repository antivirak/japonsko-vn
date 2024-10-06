screen right_side_menu_overlay():
    vbox:
        xalign 1.0 yalign 0.1
        spacing 10

        imagebutton:
            idle im.Scale("images/stats_icon_idle.png", 100, 50)
            hover im.Scale("images/stats_icon_hover.png", 100, 50)
            action Show("stats_overview")
            keyboard_focus False

        imagebutton:
            idle im.Scale("images/book_icon_idle.png", 100, 50)
            hover im.Scale("images/book_icon_hover.png", 100, 50)
            action Show("dictionary")
            keyboard_focus False