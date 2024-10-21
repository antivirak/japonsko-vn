"""renpy
init python:
"""

class Dictionary:
    def __init__(self):
        self._content = {
            "ikimašó": "pojďme",
            "šinkanzen": "japonský rychlovlak",
            "rámen": "japonská polévka s nudlemi",
            "tatami": "japonské rohože, nesmí se na ně šlapat v botech",
            "konbini": "Japonská sámoška/večerka. Známé řetězce: 7-Eleven, FamilyMart, Lawson.",
            "gaijin point": "cizinecký bod",
            "love point": "milostný bod",
            "hate point": "nenávistný bod",
            "VN": "visual novela",
            "dózo": "prosím (někomu něco nabízím)",
            "Ičiran": "řetězec rámenáren",
            "wagyu steak": "Luxusní hovězí maso, které je charakteristické svým tukovým mramorováním. "
                           "Tito býčci jsou pravidelně masírováni a je jim dopřávána jen ta nejkvalitnější péče.",
            "futon": "japonsky polštář, často polštářové matrace na sezení, či spaní",
            "ufocatcher": "automatová hra, kde pomocí jeřábové ruky a páček snažíte přesunout odměnu do výdejní jámy",
            "Ghibli": "Legendární animační studio. Autoři filmů jako je Princezna Mononoke nebo Cesta do fantazie.",
            "konbanwa": "dobrý večer",
            "kanpai": "na zdraví",
            "sumimasen": "promiňte",
            "miso": "pasta z kvašených sójových bobů, rýže a ječné slámy",
        }

    @property
    def content(self):
        return dict(sorted(
            self._content.items(),
            # ensure ch is after h and ignore case
            key=lambda x: f"h{chr(0x10FFFF)}{x[0].lower()[2:]}" if x[0].lower().startswith("ch") else x[0].lower(),
        ))

    def add_item(self, key: str, description: str):
        self._content[key] = description
