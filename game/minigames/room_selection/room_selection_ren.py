"""renpy
init python:
"""

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
    if all(len(dropdown.ignore) == len(dropdown.dropdown_list) - 1 for dropdown in dropdowns):
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
