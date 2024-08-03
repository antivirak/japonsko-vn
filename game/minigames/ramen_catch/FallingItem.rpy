init python:
        import pygame

        class FallingItem(renpy.Displayable, Collidable):
            def __init__(self, child, x, y, item_type, width, height, collidable_width, collidable_height, **kwargs):
                renpy.Displayable.__init__(self, **kwargs)
                Collidable.__init__(self, collidable_width = collidable_width, collidable_height = collidable_height)
                self.x = x
                self.y = y
                self.child = child
                self.speed = 50
                self.item_type = item_type
                self.old_st = None
                self.show = True
                self.width = width
                self.height = height
            def render(self, width, height, st, at):
                r = renpy.Render(width, height)

                if self.old_st == None:
                    self.old_st = st
                #time elapsed since last frame
                dt = st - self.old_st
                self.old_st = st

                self.y += self.speed*dt
                
                if self.show:
                    cr = renpy.render(self.child, width, height, st, at)
                    r.blit(cr, (self.x, self.y))
                    renpy.redraw(self, 0)
                # for debugging purposes draw collision rectangle, CAREFUL THIS SLOWS GAME A LOT
                #canvas = r.canvas()
                #bounds = self.get_bounds()
                #x1, y1, x2, y2 = bounds
                # Draw top line
                #canvas.line("#003366", (x1, y1), (x2, y1), width=2)
                # Draw bottom line
                #canvas.line("#003366", (x1, y2), (x2, y2), width=2)
                # Draw left line
                #canvas.line("#003366", (x1, y1), (x1, y2), width=2)
                # Draw right line
                #canvas.line("#003366", (x2, y1), (x2, y2), width=2)               
                return r
            
            def get_bounds(self):
                return (self.x, self.y + self.height/2, self.x + self.collidable_width, self.y + self.height/2 + self.collidable_height)
            
            def get_rect(self):              
                return pygame.Rect(self.x, self.y + self.height/2, self.collidable_width, self.collidable_height)

            def change_image_to_tranparent(self):
                new_child = im.Scale("empty.png", self.child.width, self.child.height)
                self.child = renpy.displayable(new_child)