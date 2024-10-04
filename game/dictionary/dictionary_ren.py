"""renpy
init python:
"""

class Dictionary:
    def __init__(self):
        self.content = {
            "ikimašó": "pojďme",
            "šinkanzen": "japonský rychlovlak",
            "rámen": "japonská polévka s nudlemi",
            "tatami": "japonské rohože, nesmí se na ně šlapat v botech",
            "konbini": "japonská sámoška/večerka",
            "gaijin point": "cizinecký bod",
            "love point": "milostný bod",
            "hate poin": "nenávistný bod",
            "VN": "visual novela",
            "dózo": "prosím (někomu něco nabízím)",
            "Ičiran": "řetězec rámenáren",
        }

    def add_item(self, key, description):
        self.content[key] = description
