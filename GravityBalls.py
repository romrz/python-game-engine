import pygame
import random
from GameEngine import GameEngine
from CircleRenderer import CircleRenderer
from RectRenderer import RectRenderer
from Physics import Physics
from Collider import Collider
from CircleCollider import CircleCollider

#
# Gravity Balls Game
# Click anywhere to create a random ball and watch the gravity make its magic
#
class GavityBalls:
    def run(self):
        self.engine = GameEngine(self.handle_events)

        self.create_ground()

        self.engine.run()

    def create_ground(self):
        ground = self.engine.create_object()
        ground.label = 'Ground'
        ground.position.x = 0
        ground.position.y = 550
        collider = Collider((0, 0, 800, 50))
        ground.add_component('Collider', collider)
        renderer = RectRenderer(800, 50, (0, 0, 0))
        ground.add_component('Renderer', renderer)

    def create_ball_on_click(self, position):
        color = tuple(random.choices(range(256), k = 3))
        self.create_ball(position, color, random.randrange(5, 30), random.randrange(1, 30))

    def create_ball(self, position, color, size, mass):
        ball = self.engine.create_object()
        ball.label = 'Ball'
        renderer = CircleRenderer(size, color)
        ball.add_component('Renderer', renderer)
        ball.position.x = position[0]
        ball.position.y = position[1]
        physics = Physics()
        physics.gravity.y = 1
        physics.mass = mass
        ball.add_component('Physics', physics)
        collider = CircleCollider(size)
        ball.add_component('Collider', collider)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.create_ball_on_click(pygame.mouse.get_pos())

if __name__ == '__main__':
    game = GavityBalls()
    game.run()
