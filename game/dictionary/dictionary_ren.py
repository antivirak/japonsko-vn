"""renpy
init python:
"""

class Dictionary:
    def __init__(self):
        self.content = dict(sorted(
            {
                "ikimašó": "pojďme",
                "šinkanzen": "japonský rychlovlak",
                "rámen": "japonská polévka s nudlemi",
                "tatami": "japonské rohože, nesmí se na ně šlapat v botech",
                "konbini": "japonská sámoška/večerka",
                "gaijin point": "cizinecký bod",
                "love point": "milostný bod",
                "hate point": "nenávistný bod",
                "VN": "visual novela",
                "dózo": "prosím (někomu něco nabízím)",
                "Ičiran": "řetězec rámenáren",
                "wague steak": "Luxusní hovězí maso, které je charakteristické svým tukovým mramorováním. "
                               "Tito býčci jsou pravidelně masírováni a je jim dopřávána jen ta nejkvalitnější péče.",
                "futon": "japonsky polštář, často polštářové matrace na sezení, či spaní",
                "ufocatcher": "automatová hra, kde pomocí jeřábové ruky a páček snažíte přesunout odměnu do výdejní jámy",
            }.items(),
            # ensure ch is after h and ignore case
            key=lambda x: f"h{chr(0x10FFFF)}{x[0].lower()[2:]}" if x[0].lower().startswith("ch") else x[0].lower(),
        ))

    def add_item(self, key: str, description: str):
        self.content[key] = description
