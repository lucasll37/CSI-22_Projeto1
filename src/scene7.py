import pygame
from obj import Obj


class Scene7:

    def __init__(self):

        self.background = Obj("gameover", 1, None, 0, 0)
        self.change_scene = False
        self.main = False
        self.justBegin = True
        self.time = 0
        self.list_group = [self.background]

    def update(self, game):

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/game_over_theme_ohio-59.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

        if self.time > 2000:
            self.change_scene = True

        self.time += 1

        if self.main:
            return 'main'

    def events(self, events, game):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and self.time > 200:
                    self.change_scene = True
                    self.main = True

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
