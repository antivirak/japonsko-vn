python early:

    from __future__ import annotations  # from typing import Self for python > 3.10


    class Person(ADVCharacter):
        def __init__(self, gender: str, **kwargs) -> None:
            super().__init__(**kwargs)
            self.name_2p = kwargs.get("name_2p")
            self.name_3p = kwargs.get("name_3p")
            self.name_4p = kwargs.get("name_4p")
            self.name_5p = kwargs.get("name_5p")
            self.name_6p = kwargs.get("name_6p")
            self.name_7p = kwargs.get("name_7p")
            self.driver = False
            self.gender = gender
            self.gaijin_points = 0
            self.love_points = {}
            self.hate_points = {}
            self.color = kwargs.get("color")

        def __eq__(self, other: object) -> bool:
            if isinstance(other, Person):
                return (self.__dict__ == other.__dict__)
            return False

        def add_love_points_for_person(self, person: Person, value: int) -> None:
            if person.name not in self.love_points:
                self.love_points[person.name] = 0
            self.love_points[person.name] += value

        def add_hate_points_for_person(self, person: Person, value: int) -> None:
            if person.name not in self.hate_points:
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
