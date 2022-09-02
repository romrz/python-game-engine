from platform import java_ver
import pygame
from Component import Component

class Collider(Component):
    def __init__(self, bounds):
        self.rect = pygame.Rect(bounds)
        self.type = 'box'
        self.trigger = False
    
    def start(self):
        self.rect = pygame.Rect(self.game_object.position.x, self.game_object.position.y, self.rect.width, self.rect.height)
    
    def update(self):
        self.rect.x = self.game_object.position.x
        self.rect.y = self.game_object.position.y

    def collides_with(self, collider):
        if collider.type == 'box':
            return self.rect.colliderect(collider.rect)
        if collider.type == 'circle':
            return self.check_circle_overlap(collider)
    
    def check_circle_overlap(self, collider):
        if self.rect.collidepoint(collider.game_object.position.x, collider.game_object.position.y):
            return True
        
        nx = max(self.rect.left, min(collider.game_object.position.x, self.rect.right))
        ny = max(self.rect.top, min(collider.game_object.position.y, self.rect.bottom))

        dx = nx - collider.game_object.position.x
        dy = ny - collider.game_object.position.y

        return (dx**2 + dy**2) <= collider.radius**2

    def debug_render(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect, width=1)
