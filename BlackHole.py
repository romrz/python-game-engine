import pygame
import math
from Component import Component

class BlackHole(Component):
    def start(self):
        self.mass = 100

    def update(self):
        pass

    def on_collision(self, game_object):
        pass