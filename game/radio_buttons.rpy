python early:

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
