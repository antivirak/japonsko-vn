
screen dropdown(dropdown_vars, rows_per_col=3, labels=('Trojlůžák', 'Dvojlůžák')):
    $ len_dropdown_vars = len(dropdown_vars)
    $ button_size = (200, 50)
    $ action = Jump('tokio1_hotel_part1')
    textbutton "Pokračovat":
        xysize button_size
        xalign .95 yalign .95
        action Function(action_if_all_selected, dropdown_vars, action)
    textbutton "Reset":
        xysize button_size
        xalign .85 yalign .95
        action Jump('problemubytovani_action')

    for count, dropdown in enumerate(dropdown_vars):
        $ int_div_count_rows = count // rows_per_col
        $ fraction = count / rows_per_col - int_div_count_rows
        $ y_pos = .5 - (.3 * fraction)
        $ x_pos = 300 + 500 * (int_div_count_rows)
        $ selected_item = dropdown.selected_item
        $ label = labels[int_div_count_rows]
        # Assign labels only to first dropdown in each column (headers).
        # Note that we are adding them from bottom row.
        $ label = label if count in [
            *[rows_per_col * _count - 1 for _count in range(len_dropdown_vars)],
            len_dropdown_vars - 1,
        ] else ""
        $ spacing = 10

        vbox:
            label label
            yalign y_pos
            xpos x_pos
            spacing spacing
            frame:
                if not dropdown.expanded:
                    ysize 80
                    textbutton selected_item.value:
                        xysize button_size
                        text_style style.button[selected_item.value]
                        action Function(setattr_safe, dropdown, 'expanded', not dropdown.expanded, dropdown_vars)
                else:
                    ysize 0
                    null width 0 height 0 

            if dropdown.expanded:
                frame:
                    ypos 50 + (30 - spacing * count % 3)
                    vbox:
                        for item in dropdown.dropdown_list:
                            if item.value in dropdown.ignore:
                                continue
                            $ actions = [
                                Function(setattr, dropdown, 'selected_item', item),
                                Function(setattr, dropdown, 'expanded', False),
                            ]
                            for current_dropdown in dropdown_vars:
                                if current_dropdown == dropdown:
                                    continue
                                $ actions.extend([
                                    Function(current_dropdown.rm_item, item.value),
                                    Function(current_dropdown.add_item, dropdown.selected_item.value)
                                    if dropdown.selected_item.value != item.value else NullAction(),
                                ])

                            if item.action:  # not used now
                                $ actions.append(item.action)

                            textbutton item.value:
                                xysize button_size
                                text_style style.button[item.value]
                                action actions
