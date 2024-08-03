init python:
        import pygame

        class Bowl(renpy.Displayable, Collidable):
            def __init__(self, child, x, y, width, height, collidable_width, collidable_height, **kwargs):
                renpy.Displayable.__init__(self, **kwargs)
                Collidable.__init__(self, collidable_width = collidable_width, collidable_height = collidable_height)
                self.x = x
                self.y = y
                self.width = width
                self.height = height
                self.child = child
                self.speed = 200  # Movement speed of the bowl
                self.old_st = None

            def render(self, width, height, st, at):
                if self.old_st is None:
                    self.old_st = st
                # Time elapsed since last frame
                dt = st - self.old_st
                self.old_st = st  

                # Ensure the bowl stays within screen bounds
                self.x += self.speed*dt
                self.x = max(0, min(self.x, config.screen_width - item_counter_hbox_width - self.width))

                cr = renpy.render(self.child, width, height, st, at)
                r = renpy.Render(width, height)
                r.blit(cr, (self.x, self.y))

                
                # for debugging purposes draw collision rectangle
                
                # canvas = r.canvas()
                
                # bounds = self.get_bounds()
            
                # x1, y1, x2, y2 = bounds
                # Draw top line              
                # canvas.line("#003366", (x1, y1), (x2, y1), width=2)
                # Draw bottom line               
                # canvas.line("#003366", (x1, y2), (x2, y2), width=2)
                # Draw left line             
                # canvas.line("#003366", (x1, y1), (x1, y2), width=2)
                # Draw right line          
                # canvas.line("#003366", (x2, y1), (x2, y2), width=2)
                    
                renpy.redraw(self, 0)
                
                return r

            def event(self, ev, x, y, st):
                if renpy.map_event(ev, "input_left"):
                    if self.speed > 0:      
                        self.speed = -self.speed
                elif renpy.map_event(ev, "input_right"):
                    self.speed = abs(self.speed)

            def get_bounds(self):
                print(self.collidable_width)

                return (self.x + 30, self.y + 32, self.x + self.collidable_width,  self.y + 32 + self.collidable_height)
            
            def get_rect(self):              
                return pygame.Rect(self.x + 30, self.y + 32, self.collidable_width, self.collidable_height)