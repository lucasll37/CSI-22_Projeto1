import pygame
from obj import Obj
from cloud import Cloud
import random


class Scene4:
    
    def __init__(self):
  
        self.background = Obj("sky", 1, None, 0, 0)
        self.cloud1 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
        # self.cloud2 = Obj("cloud2", 1, None, 0, 0)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = [self.background, self.cloud1]

    def moveCloud1(self):
        self.cloud1.sprite.rect[1] -= 4

    def update(self):

        if self.justBegin:
            # pygame.mixer.music.stop()
            # pygame.mixer.music.load("sounds/whatever.ogg")
            # pygame.mixer.music.play(-1)
            self.justBegin = False

        self.moveCloud1()
            
        # if self.time > 300:    
        #     self.change_scene = True

        # self.time += 1


    def events(self, events):
        for event in events:
            pass

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)
