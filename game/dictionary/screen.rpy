screen dictionary():
    modal True
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            label "Slovník"

            # Scrollable list
            viewport:
                xmaximum 800
                ymaximum 520
                draggable True
                mousewheel True
                scrollbars "vertical"
                vbox:
                    for key, value in dictionary.content.items():
                        hbox:
                            spacing 10
                            label str(key) + ' - '
                            label str(value)


            textbutton "Close" action Hide("dictionary")