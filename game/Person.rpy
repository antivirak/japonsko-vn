init python:

    class Person(ADVCharacter):
        def __init__(self, gender, **kwargs):
            super().__init__(**kwargs)
            self.gender = gender
            self.gaijin_points = 0
            self.love_points = {}
            self.hate_points = {}

        def add_love_points_for_person(self, person, value):
            if person.name not in self.love_points:
                self.love_points[person.name] = 0
            self.love_points[person.name] += value

        def add_hate_points_for_person(self, person, value):
            if person.name not in self.love_points:
                self.hate_points[person.name] = 0
            self.hate_points[person.name] += value
        
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