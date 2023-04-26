import random

import pygame
from obj import Obj
from plane import Plane


class Scene3:

    def __init__(self):

        self.background = Obj("instructions", 1, None, 0, 0)
        self.change_scene = False
        self.time = 0
        self.list_group = [self.background]

    def update(self, game):
        if self.time > 400:
            self.change_scene = True

        self.time += 1

    def events(self, events, game):
        for event in events:
            pass

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
