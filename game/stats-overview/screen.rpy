screen stats_button_overlay:
    hbox:
        xalign 1.0 yalign 0.1
        imagebutton:
            idle im.Scale("images/stats_icon_idle.png", 100, 50)
            hover im.Scale("images/stats_icon_hover.png", 100, 50)
            action Show("stats_overview")
            keyboard_focus False
screen stats_overview:
    modal True
    frame:
        xalign 0.5 yalign 0.5
        vbox:
            label "[j.name]"

            hbox:
                add im.Scale("images/gaijin_points_icon.png", 40, 40)
                label "Gaijin Points: "
                text "[j.gaijin_points]"

            # Header row for the table
            hbox:
                xalign 0.5
                spacing 50
                label "Person" xysize (100, None)
                hbox:
                    add im.Scale("images/love_points_icon.png", 40, 40)
                    label "Love Points" xysize (210, None)
                hbox:
                    add im.Scale("images/hate_points_icon.png", 40, 40)
                    label "Hate Points" xysize (210, None)

            for person in persons:
                hbox:
                    spacing 200
                    label person.name xysize (100, None)
                    text str(j.get_love_points_for_person(person.name))
                    text str(j.get_hate_points_for_person(person.name))

            textbutton "Close" action Hide("stats_overview")