import pygame
from Renderer import Renderer

class CircleRenderer(Renderer):
    def __init__(self, radius = 10, color = (0, 0, 0, 255)):
        self.radius = radius
        self.color = pygame.Color(color)

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.game_object.position, self.radius)
