import pygame
from window import Window
from scene0 import Scene0
from scene1 import Scene1
from scene2 import Scene2
from scene3 import Scene3
from scene4 import Scene4
from scene5 import Scene5

class Game:

    def __init__(self, size, name):
        
        pygame.init()
        pygame.mixer.init()

        self.scenes = [Scene0(), Scene1(), Scene2(), Scene3()]
        self.window = Window(size, name, self.scenes)

    def start(self):
        self.window.update()