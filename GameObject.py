import pygame
import importlib

class GameObject:

    def __init__(self, engine, label = ''):
        self.engine = engine
        self.label = label
        self.position = pygame.math.Vector2(0, 0)
        self.components = {}

    def add_component(self, type, component = None):
        component = component or self.create_component(type)
        component.game_object = self
        component.start()
        self.components[type] = component

    def get_component(self, type):
        return self.components.get(type)
    
    def create_component(self, type):
        return getattr(importlib.import_module(type), type)()

    def update(self):
        for component in self.components.values():
            component.update()

    def render(self, screen):
        renderer = self.get_component('Renderer')

        if renderer != None:
            renderer.render(screen)

        # collider = self.get_component('Collider')
        # if collider != None:
            # collider.debug_render(screen)

    def notify_collision(self, game_object):
        for component in self.components.values():
            component.on_collision(game_object)
