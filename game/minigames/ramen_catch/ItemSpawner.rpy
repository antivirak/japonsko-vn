init python:

    from __future__ import annotations
    import random

    class ItemSpawner:
        def __init__(self, spawn_interval: float) -> None:
            self.items = []
            self.spawn_interval = spawn_interval # in seconds
            self.item_attributes = {
                    "noodle": {"image": "noodle.png", "width": 100, "height": 100, "collidable_width": 100, "collidable_height": 50},
                    "dashi": {"image": "dashi.png", "width": 150, "height": 100, "collidable_width": 150, "collidable_height": 50},
                    "chaschu": {"image": "chaschu.png", "width": 150, "height": 100, "collidable_width": 150, "collidable_height": 50},
                    "garlic": {"image": "garlic.png", "width": 75, "height": 75, "collidable_width": 75, "collidable_height": 32},
                    "white_onion": {"image": "white_onion.png", "width": 150, "height": 100, "collidable_width": 150, "collidable_height": 50},
                    "green_onion": {"image": "green_onion.png", "width": 100, "height": 75, "collidable_width": 100, "collidable_height": 35},
                    "chilli": {"image": "chilli.png", "width": 32, "height": 132, "collidable_width": 32, "collidable_height": 66}
                }
            self.loaded_images = {} # Load images only once
            print("init ItemSpawner")


        def get_image(self, image_path: str, width: int, height: int) -> renpy.Displayable:
            if image_path not in self.loaded_images:
                self.loaded_images[image_path] = im.Scale(image_path, width, height)
            return self.loaded_images[image_path]

        def spawn_item(self) -> None:
            new_item = self.get_random_item()
            self.items.append(new_item)
            ui.add(new_item)

        def get_random_item(self) -> FallingItem:
            item_type = random.choice(list(self.item_attributes.keys()))
            attributes = self.item_attributes[item_type]
            image_displayable = self.get_image(attributes["image"], attributes["width"], attributes["height"])
            return FallingItem(image_displayable,
                                x = random.randint(0, config.screen_width - item_counter_hbox_width - attributes["width"]),
                                y = 0, item_type = item_type, width = attributes["width"], height
                                 = attributes["height"], collidable_width = attributes["collidable_width"], collidable_height= attributes["collidable_height"])
        def reset_items(self):
            self.items = []

    
