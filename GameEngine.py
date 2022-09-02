import sys
import pygame
from GameObject import GameObject

class GameEngine:
    def __init__(self, handle_events_callback):
        self.game_objects = []

        self.handle_events_callback = handle_events_callback

        pygame.init()

        # Settings
        self.FPS = 60
        self.screen_size = (800, 600)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.bg_color = (255, 255, 255)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Game Engine')

    def create_object(self):
        game_object = GameObject(self)
        self.game_objects.append(game_object)
        return game_object
    
    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.check_collisions()
            self.render()

    def handle_events(self):
        events = pygame.event.get()

        self.handle_events_callback(events)

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

    def check_collisions(self):
        for object1 in self.game_objects:
            collider1 = object1.get_component('Collider')

            if collider1 == None:
                continue

            for object2 in self.game_objects:
                if object2 == object1:
                    continue

                collider2 = object2.get_component('Collider')

                if collider2 == None:
                    continue

                if collider1.collides_with(collider2):
                    object1.notify_collision(object2)

    def update(self):
        for game_object in self.game_objects:
            game_object.update()

    def render(self):
        self.screen.fill(self.bg_color)

        for game_object in self.game_objects:
            game_object.render(self.screen)

        pygame.display.flip()

    def remove_object(self, object):
        self.game_objects.remove(object)
