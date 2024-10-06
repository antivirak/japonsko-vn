init python:
    from typing import Optional
    from collections.abc import Callable, Hashable


    class DropdownItem:
        def __init__(self, value: str, action: Optional[Callable] = None, selected: bool = False) -> None:
            self.value = value
            self.action = action
            self.selected = selected
            self.color = None


    class Dropdown:
        def __init__(self, dropdown_list: list[DropdownItem], color_map: dict) -> None:
            self.dropdown_list = dropdown_list
            self.expanded = False
            self.selected_item = object()
            self.selected_item.value = ''
            self.ignore = {''}
            self.color_map = color_map
            set_button_styles(color_map)

        def __eq__(self, other: object) -> bool:
            if not isinstance(other, Dropdown):
                return False
            return (
                self.selected_item.value == other.selected_item.value
                and self.expanded == other.expanded  # noqa W503
            )

        def rm_item(self, item: Hashable) -> None:
            self.ignore.add(item)

        def add_item(self, item: Hashable) -> None:
            if item in self.ignore:
                self.ignore.remove(item)


    def action_if_all_selected(dropdowns: list[Dropdown], action: Callable) -> None:
        if all(len(dropdown.ignore) == 4 for dropdown in dropdowns):
            action()


    def resolve_room_selection(dropdowns: list[str]) -> tuple[str, list[str]]:
        idx = dropdowns.index(j.name)
        assert idx > -1, f"Name {j.name} not found in dropdowns {dropdowns}"
        trojluzak = idx < 3
        return (
            "Trojlůžák" if trojluzak else "Dvojlůžák",
            dropdowns[:3] if trojluzak else dropdowns[3:],
        )


    def set_button_styles(color_map: dict) -> None:
        for char, color in color_map.items():
            style.button[char].color = color


    def setattr_safe(obj, attr, val, dropdowns):
        """Forbid the possibility to expand more than one dropdown at a time."""
        if all(not current_dropdown.expanded for current_dropdown in dropdowns if current_dropdown != obj):
            setattr(obj, attr, val)


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
