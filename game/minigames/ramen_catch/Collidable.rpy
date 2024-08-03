init -1 python:

        from abc import ABC, abstractmethod

        class Collidable(ABC):
            def __init__(self, collidable_width, collidable_height):
                self.collidable_width = collidable_width
                self.collidable_height = collidable_height

            @abstractmethod
            def get_rect(self):
                pass
