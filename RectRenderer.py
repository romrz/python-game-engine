import pygame
from Renderer import Renderer

class RectRenderer(Renderer):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.game_object.position.x, self.game_object.position.y, self.width, self.height))
