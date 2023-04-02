import pygame
from obj import Obj

class Scene2:
    
    def __init__(self):
        self.bg = Obj("assets/free_plane_sprite/png/background", 1, 0, 0, True)
        self.plane = Obj("assets/free_plane_sprite/png/Plane/plane", 2, 20, 20, True)
        self.change_scene = False
        self.list_group = [self.bg, self.plane]

    def events(self, events):
        for event in events:
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True

    def update(self):
        pass

    def draw(self, window):
        for group in self.list_group:
            group.group.draw(window)