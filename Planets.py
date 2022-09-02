import pygame
import random
from GameEngine import GameEngine
from CircleRenderer import CircleRenderer
from RectRenderer import RectRenderer
from Physics import Physics
from Collider import Collider
from CircleCollider import CircleCollider
from Planet import Planet
from BlackHole import BlackHole

#
# Planets Game
# Click anywhere to create a random planet and make it orbit the black hole
#
class Planets:
    def run(self):
        self.engine = GameEngine(self.handle_events)

        self.create_black_hole()

        self.engine.run()

    def create_black_hole(self):
        blackhole_field = self.engine.create_object()
        blackhole_field.label = 'Black Hole Field'
        blackhole_field.position.x = 400
        blackhole_field.position.y = 300
        collider = CircleCollider(2000)
        collider.trigger = True
        blackhole_field.add_component('Collider', collider)
        blackhole_field.add_component('BlackHole', BlackHole())

        blackhole = self.engine.create_object()
        blackhole.label = 'Black Hole'
        blackhole.position.x = 400
        blackhole.position.y = 300
        collider = CircleCollider(25)
        collider.trigger = True
        blackhole.add_component('Collider', collider)
        renderer = CircleRenderer(25, (0, 0, 0))
        blackhole.add_component('Renderer', renderer)

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
        planet = Planet()
        ball.add_component('Planet', planet)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.create_ball_on_click(pygame.mouse.get_pos())

if __name__ == '__main__':
    game = Planets()
    game.run()
