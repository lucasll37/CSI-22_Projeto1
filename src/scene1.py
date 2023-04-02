import pygame
from obj import Obj

class Scene1:
    
    def __init__(self):
        self.background = Obj("assets/free_plane_sprite/png/background", 1, 0, 0, True)
        self.plane = Obj("assets/free_plane_sprite/png/Plane/plane", 2, 20, 20, True)
        self.change_scene = False
        self.list_group = [self.background, self.plane]

    def events(self, events):
        for event in events:
            if event == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True

    def update(self):
        self.background.sprite.rect[0] -= 5

    def draw(self, window):
        for group in self.list_group:
            group.group.draw(window)

