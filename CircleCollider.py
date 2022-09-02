import pygame
import math
from Component import Component

class CircleCollider(Component):
    def __init__(self, radius):
        self.radius = radius
        self.type = 'circle'
        self.trigger = False

    def debug_render(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.game_object.position, self.radius, width=1)
    
    def collides_with(self, collider):
        if collider.type == 'box':
            return collider.check_circle_overlap(self)
        if collider.type == 'circle':
            return math.sqrt((self.game_object.position.x - collider.game_object.position.x)**2 + (self.game_object.position.y - collider.game_object.position.y)**2) <= (self.radius + collider.radius)
    
