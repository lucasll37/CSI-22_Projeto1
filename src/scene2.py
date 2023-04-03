import pygame
from obj import Obj
from plane import Plane
import random

class Scene1:
    
    def __init__(self):
        self.background = Obj("background", 1, None, 0, 0)
        self.time = 0

  

    def update(self):
        if self.time > 800:    
            self.change_scene = True

        self.time += 1


    def events(self, events):
        for event in events:
            pass

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)