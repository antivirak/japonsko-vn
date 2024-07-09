"""renpy
init python:
"""


class RadioButtonGroup:
    """A class to manage a group of radio buttons."""
    def __init__(self, options: list[str], actions=None):
        """Initializes the RadioButtonGroup with given options."""
        self.selected: list[int] = []
        self.options = list(enumerate(options))
        len_options = len(options)
        assert (
            actions is None or len(actions) == len_options,
            "Actions must be undefined or have the same length as options."
        )
        if actions is None:
            self.actions = [NullAction() for _ in range(len_options)]
        else:
            self.actions = actions[:len_options]

    def set_option(self, option_id: int, max_choice: int = 1):
        """Selects or deselects an option based on its ID."""
        if option_id in self.selected:
            self.selected.remove(option_id)
        else:
            if len(self.selected) >= max_choice:
                num_to_remove = len(self.selected) - max_choice + 1
                del self.selected[:num_to_remove]
            self.selected.append(option_id)

    def is_selected(self, option_id: int):
        """Checks if a given option ID is selected."""
        return option_id in self.selected

    def get_selected_index(self):
        """Returns the indices of selected options."""
        return sorted(self.selected)

    def get_selected_values(self):
        """Returns the values of selected options."""
        selection = self.get_selected_index()
        return [self.options[idx][1] for idx in selection]


class RadioButtonGroupSpicy(RadioButtonGroup):
    def __init__(self, options: list[str], actions=None) -> None:
        super().__init__(options, actions)
        self.spiciness = self.reset_spiciness()
        self.textbutton_backgrounds = []
        self.hovered = {}

    def reset_spiciness(self) -> str:
        self.spiciness = '      '
        return self.spiciness

    def set_spiciness(self, num: int) -> None:
        self.spiciness = f'  {num}' if num != 10 else f' {num}'

    def get_spiciness(self) -> float:
        if spiciness := self.spiciness.strip():
            return float(spiciness)
        spiciness = self.selected[0]
        if spiciness == 0:
            return .0
        if spiciness == 1:
            return .5
        return float(spiciness - 1)

    def set_hovered(self, option_id: int, val: bool) -> None:
        self.hovered[option_id] = val

    def is_hovered(self, option_id: int) -> bool:
        return self.hovered.get(option_id, False)


def get_spiciness_input(rb_group: RadioButtonGroupSpicy, show: bool) -> None:
    if show:
        renpy.call_in_new_context('switch_context', rb_group)


def show_hbox(
    rb_group: RadioButtonGroupSpicy, h_spacing: int, max_choice: int, show_input: bool = False,
) -> None:
    len_options = len(rb_group.options)
    with ui.hbox(spacing=h_spacing):
        for count, (option_id, option_image) in enumerate(rb_group.options):
            # with ui.vbox(align=(.5, 0)):
            is_option_selected = rb_group.is_selected(option_id)
            tint_factor = 1 if is_option_selected else .5
            tinted_image = im.MatrixColor(  # TODO im.* deprecated
                option_image, im.matrix.tint(tint_factor, tint_factor, tint_factor),
            )
            idle_image = tinted_image if is_option_selected else "images/transparent_image.png"
            actions = [
                Function(rb_group.set_option, option_id, max_choice),
                rb_group.actions[option_id],
            ]
            if show_input and count != len_options - 1:
                actions.extend([
                    rb_group.reset_spiciness,
                    Jump('ichiran_selection_minigame'),
                ])
            if show_input and count == len_options - 1:
                # in spiciness selection, we show textbutton instead of imagebutton,
                # so user can select freeform value from 3 to 10
                actions.append(Function(get_spiciness_input, rb_group, show_input))
                rb_group.textbutton_backgrounds = [idle_image, option_image, tinted_image]
                ui.textbutton(
                    rb_group.spiciness,
                    at=radio_buttons,
                    background=rb_group.textbutton_backgrounds[
                        2 if rb_group.is_hovered(option_id) else rb_group.is_selected(option_id)
                    ],
                    text_style='text_red',
                    action=actions,
                    hovered=Function(rb_group.set_hovered, option_id, True),
                    unhovered=Function(rb_group.set_hovered, option_id, False),
                )
            else:
                ui.imagebutton(
                    at=radio_buttons,
                    idle=idle_image,
                    hover=tinted_image,
                    selected=option_image,
                    action=actions,
                )


def show_vbox(
    rb_groups: list[RadioButtonGroupSpicy],
    align_x: float, align_y: float, v_spacing: int, h_spacing: int, max_choice: int,
) -> None:
    count = 0
    with ui.vbox(spacing=v_spacing, align=(align_x, align_y)):
        for count, rb_group in enumerate(rb_groups):
            if rb_group is None:
                break
            show_hbox(rb_group, 53 if count == 3 else h_spacing, max_choice)

    with ui.vbox(spacing=31, align=(align_x, .84)):
        for not_show_input, rb_group in enumerate(rb_groups[count + 1:]):
            show_hbox(rb_group, h_spacing, max_choice, show_input=not not_show_input)


def show_ichiran_menu(rb_groups: list[RadioButtonGroupSpicy], max_choice: int = 1) -> None:
    show_vbox(
        rb_groups=rb_groups,
        align_x=.55, align_y=.36, v_spacing=-8, h_spacing=4, max_choice=max_choice,
    )


def try_float(value: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return float(-1)
