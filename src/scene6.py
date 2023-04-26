import pygame
from obj import Obj
import random

class Scene6:
    
    def __init__(self):

        self.background = Obj("gameover", 1, None, 0, 0)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = [self.background]


    def PlayAgain(self, event, game):
        print(game.gameStatus)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                pass
                    
            else:
                self.change_scene = True

    def update(self, game):
        
        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/intro.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False
            
        # if self.time > 300:    
        #     self.change_scene = True

        if game.gameStatus != "over":
            print(game.gameStatus) ##########
            self.change_scene = True

        self.time += 1


    def events(self, events, game):
        for event in events:
            self.PlayAgain(event, game)

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)
