init python:
    from __future__ import annotations

    class CollisionDetector(renpy.Displayable):
        def __init__(self, spawner, bowl, counter, **kwargs):
            super().__init__(**kwargs)
            self.spawner = spawner
            self.bowl = bowl
            self.counter = counter

        def render(self, width, height, st, at):
            self.detect_collisions()

            # Create and return an empty render object
            r = renpy.Render(width, height)
            renpy.redraw(self, 0)
            return r

        def detect_collisions(self):
            bowl_rect = self.bowl.get_rect()
            rect_items = map(lambda item: (item.get_rect(), item), self.spawner.items)

            for rect, item in rect_items:
                collided = bowl_rect.colliderect(rect)

                if collided:                  
                    if self.counter.get_target_amount(item.item_type) > 0 and self.counter.get_counter(item.item_type) < self.counter.get_target_amount(item.item_type):
                        self.counter.increase_counter(item.item_type)
                        renpy.play('audio/slurp.mp3')
                        item.show = False
                        ui.remove(item)              
                        self.spawner.items.remove(item)
                        renpy.restart_interaction()  # Redraw screen - bcs it takes too long to rerender for example the item number in vbox
                        if self.counter.all_counters_reached_target_amount():
                            renpy.play('audio/victory-8bit.mp3')
                            renpy.jump("ramencatch_won")         
                    elif self.counter.get_target_amount(item.item_type) == 0:
                        renpy.play('audio/wrong.mp3')
                        renpy.call_in_new_context("ramencatch_lost")               
                    continue

