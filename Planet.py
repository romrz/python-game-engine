import pygame
import math
from Component import Component

class Planet(Component):

    def update(self):
        self.physics = self.game_object.get_component('Physics')

    def on_collision(self, game_object):
        if game_object.label == 'Black Hole':
            self.game_object.engine.remove_object(self.game_object)
        
        if game_object.label == 'Black Hole Field':
            force = (game_object.get_component('BlackHole').mass * self.physics.mass) / math.sqrt((self.game_object.position.x - 400)**2 + (self.game_object.position.y - 300)**2)
            forceX = force * math.cos(math.atan2(300 - self.game_object.position.y, 400 - self.game_object.position.x))
            forceY = force * math.sin(math.atan2(300 - self.game_object.position.y, 400 - self.game_object.position.x))
            self.physics.add_force(pygame.math.Vector2(forceX, forceY))

