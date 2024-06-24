init python:

    class Person:
        def __init__(self, character, gender):
            self.char = character
            self.gender = gender
            self.gaijin_points = 0
            self.love_points = {}
            self.hate_points = {}

        def add_love_points_for_person(self, person, value):
            if person.char.name not in self.love_points:
                self.love_points[person.char.name] = 0
            self.love_points[person.char.name] += value

        def add_hate_points_for_person(self, person, value):
            if person.char.name not in self.love_points:
                self.hate_points[person.char.name] = 0
            self.hate_points[person.char.name] += value
        
        def get_hate_points_table(self):
            if not self.hate_points:
                return "Nemáš žádné hate points.."
            table_lines = [f"{name}: {points}" for name, points in self.hate_points.items()]
            return "\n".join(table_lines)
    
        def get_love_points_table(self):
            if not self.love_points:
                return "Nemáš žádné love points.."
            table_lines = [f"{name}: {points}" for name, points in self.love_points.items()]
            return "\n".join(table_lines)