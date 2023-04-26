import pygame
from obj import Obj


class Scene0:

    def __init__(self):

        self.background = Obj("intro2", 1, None, 0, 0)
        self.change_scene = False
        self.list_group = [self.background]
        self.justBegin = True

    def update(self, game):
        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/intro.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

    def events(self, events, game):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True
                    return ' '

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
