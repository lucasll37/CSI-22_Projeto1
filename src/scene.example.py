import pygame
from obj import Obj
import random

############################################################################################
#
# ADICIONAR "SceneN()" na lista armazenada na variável "self.scenes" do arquivo "game.py"
#
############################################################################################

class SceneN:
    
    def __init__(self):

        # self.background = Obj("continua", 1, None, 0, 0)
        # self.change_scene = False
        # self.justBegin = True
        self.time = 0
        # self.list_group = [self.background]

    def update(self):
        
        # if self.justBegin:
            # pygame.mixer.music.stop()
            # pygame.mixer.music.load("sounds/whatever.ogg")
            # pygame.mixer.music.play(-1)
        #     self.justBegin = False
            
        # if self.time > 300:    
        #     self.change_scene = True

        self.time += 1


    def events(self, events):
        for event in events:
            pass

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)
