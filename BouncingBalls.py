import pygame
import random
from GameEngine import GameEngine
from CircleRenderer import CircleRenderer
from RectRenderer import RectRenderer
from Physics import Physics
from Collider import Collider
from CircleCollider import CircleCollider

#
# Bouncing Balls Game
# Click anywhere to create a random ball and watch them bounce!
#
class BouncingBalls:
    def run(self):
        self.engine = GameEngine(self.handle_events)

        self.create_walls()

        self.engine.run()

    def create_walls(self):
        self.create_wall(0, 0, 800, 20)
        self.create_wall(0, 0, 20, 600)
        self.create_wall(0, 580, 800, 20)
        self.create_wall(780, 0, 20, 600)

    def create_wall(self, x, y, width, height):
        wall = self.engine.create_object()
        wall.label = 'Wall'
        wall.position.x = x
        wall.position.y = y
        collider = Collider((0, 0, width, height))
        wall.add_component('Collider', collider)
        renderer = RectRenderer(width, height, (0, 0, 0))
        wall.add_component('Renderer', renderer)

    def create_ball_on_click(self, position):
        color = tuple(random.choices(range(256), k = 3))
        self.create_ball(position, color, (random.randrange(-10, 10), random.randrange(-10, 10)), random.randrange(5, 30), random.randrange(1, 30))

    def create_ball(self, position, color, velocity, size, mass):
        ball = self.engine.create_object()
        ball.label = 'Ball'
        renderer = CircleRenderer(size, color)
        ball.add_component('Renderer', renderer)
        ball.position.x = position[0]
        ball.position.y = position[1]
        physics = Physics()
        physics.velocity.x = velocity[0]
        physics.velocity.y = velocity[1]
        physics.mass = mass
        ball.add_component('Physics', physics)
        collider = CircleCollider(size)
        ball.add_component('Collider', collider)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.create_ball_on_click(pygame.mouse.get_pos())

if __name__ == '__main__':
    game = BouncingBalls()
    game.run()
