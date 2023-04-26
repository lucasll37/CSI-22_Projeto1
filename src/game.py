import pygame
from scene0 import Scene0
from scene1 import Scene1
from scene2 import Scene2
from scene3 import Scene3
from scene4 import Scene4
from scene8 import Scene8
from window import Window


class Game:

    def __init__(self, size, name):

        pygame.init()
        pygame.mixer.init()

        self.gameStatus = "onPlay"
        self.scenes = [Scene0(), Scene8(), Scene1(),
                       Scene2(), Scene3(), Scene4()]
        self.window = Window(self, size, name, self.scenes)

    def start(self):
        self.window.update()
