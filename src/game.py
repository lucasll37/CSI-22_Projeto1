# The Game class initializes a game with multiple scenes and a window.
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

        # These lines of code are initializing the Pygame library and its mixer module, setting the
        # game status to "onPlay", creating a list of scenes for the game, and creating a window
        # object for the game with the specified size, name, and scenes.
        pygame.init()
        pygame.mixer.init()

        self.gameStatus = "onPlay"
        self.scenes = [Scene0(), Scene8(), Scene1(),
                       Scene2(), Scene3(), Scene4()]
        self.window = Window(self, size, name, self.scenes)

    def start(self):
        """
        This function updates the window.
        """
        self.window.update()
