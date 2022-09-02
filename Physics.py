import pygame
import math
from Component import Component

class Physics(Component):
    def __init__(self):
        self.mass = 0
        self.forces = []
        self.gravity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.velocity = pygame.math.Vector2(0, 0)

        self.updated = False

    def update(self):
        self.updated = False

        force = self.calculate_forces()

        self.acceleration.x = force.x / self.mass + self.gravity.x
        self.acceleration.y = force.y / self.mass + self.gravity.y
        self.velocity = self.velocity + self.acceleration
        self.game_object.position = self.game_object.position + self.velocity

        # force = (1000.0 * self.mass) / math.sqrt((self.game_object.position.x - 400)**2 + (self.game_object.position.y - 300)**2)
        # forceX = force * math.cos(math.atan2(300 - self.game_object.position.y, 400 - self.game_object.position.x))
        # forceY = force * math.sin(math.atan2(300 - self.game_object.position.y, 400 - self.game_object.position.x))

        self.forces = []
    
    def calculate_forces(self):
        sum_forces = pygame.math.Vector2(0, 0)

        for force in self.forces:
            sum_forces += force

        return sum_forces
    
    def add_force(self, force):
        self.forces.append(force)

    def on_collision(self, game_object):
        collider = game_object.get_component('Collider')

        if collider.trigger:
            return
        
        if self.game_object.get_component('Collider').trigger:
            return

        if collider.type == 'box':
            if self.game_object.position.x < collider.rect.left and self.game_object.position.y > collider.rect.top and self.game_object.position.y < collider.rect.bottom:
                self.velocity.x *= -1
            if self.game_object.position.x > collider.rect.right and self.game_object.position.y > collider.rect.top and self.game_object.position.y < collider.rect.bottom:
                self.velocity.x *= -1
            if self.game_object.position.y < collider.rect.top and self.game_object.position.x > collider.rect.left and self.game_object.position.y < collider.rect.right:
                self.velocity.y *= -1
            if self.game_object.position.y > collider.rect.bottom and self.game_object.position.x > collider.rect.left and self.game_object.position.y < collider.rect.right:
                self.velocity.y *= -1
        
        if collider.type == 'circle':
            if self.updated:
                return

            cx1 = self.game_object.position.x
            cy1 = self.game_object.position.y
            cx2 = game_object.position.x
            cy2 = game_object.position.y

            d = math.sqrt((cx1 - cx2)**2 + (cy1 - cy2)**2)

            nx = (cx2 - cx1) / d
            ny = (cy2 - cy1) / d

            vx1 = self.velocity.x
            vy1 = self.velocity.y
            vx2 = game_object.get_component('Physics').velocity.x
            vy2 = game_object.get_component('Physics').velocity.y

            p = 2 * (vx1 * nx + vy1 * ny - vx2 * nx - vy2 * ny) / (self.mass + game_object.get_component('Physics').mass)

            self.velocity.x = (vx1 - p * game_object.get_component('Physics').mass * nx)
            self.velocity.y = (vy1 - p * game_object.get_component('Physics').mass * ny)
            game_object.get_component('Physics').velocity.x = (vx2 + p * self.mass * nx)
            game_object.get_component('Physics').velocity.y = (vy2 + p * self.mass * ny)

            self.updated = True
            game_object.get_component('Physics').updated = True
