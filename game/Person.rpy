init python:

    from __future__ import annotations  # from typing import Self for python > 3.10


    class Person(ADVCharacter):
        def __init__(self, gender: str, **kwargs) -> None:
            super().__init__(**kwargs)
            self.gender = gender
            self.gaijin_points = 0
            self.love_points = {}
            self.hate_points = {}

        def add_love_points_for_person(self, person: Person, value: int) -> None:
            if person.name not in self.love_points:
                self.love_points[person.name] = 0
            self.love_points[person.name] += value

        def add_hate_points_for_person(self, person: Person, value: int) -> None:
            if person.name not in self.love_points:
                self.hate_points[person.name] = 0
            self.hate_points[person.name] += value

        def get_hate_points_table(self) -> str:
            if not self.hate_points:
                return "Nemáš žádné hate points.."
            table_lines = [f"{name}: {points}" for name, points in self.hate_points.items()]
            return "\n".join(table_lines)

        def get_love_points_table(self) -> str:
            if not self.love_points:
                return "Nemáš žádné love points.."
            table_lines = [f"{name}: {points}" for name, points in self.love_points.items()]
            return "\n".join(table_lines)

        def show_all_points(self) -> str:
            return (
                f"aktuální LP: {self.get_love_points_table()}"
                f"\naktuální HP: {self.get_hate_points_table()}"
                f"\naktuální GP: {self.gaijin_points if self.gaijin_points else 'Nemáš žádné gaijin points..'}"
            )
