# The Window class creates a game window and manages the scenes and events within the game.
import pygame

from scene6 import Scene6
from scene7 import Scene7


class Window:

    def __init__(self, game, size, name, scenes):
        """
        This function initializes a game window with a specified size, name, and scenes.

        :param game: The game object that controls the overall game logic and state
        :param size: The size parameter is a tuple that specifies the width and height of the game
        window. For example, size = (800, 600) would create a window that is 800 pixels wide and 600
        pixels tall
        :param name: The name of the game window that will be displayed at the top of the window
        :param scenes: The "scenes" parameter is likely a list or dictionary containing the different
        scenes or levels of the game. Each scene would have its own set of game objects, background,
        music, and other properties that define the gameplay experience. The game loop would iterate
        through these scenes, updating and rendering the game objects
        """
        self.window = pygame.display.set_mode(size)
        self.title = pygame.display.set_caption(name)
        self.game = game
        self.scenes = scenes
        self.loop = True
        self.fps = pygame.time.Clock()

    def globalEvents(self, events):
        """
        This function checks if the event type is pygame.QUIT and sets the loop variable to False if it
        is.

        :param events: The "events" parameter is a list of events that have occurred in the Pygame event
        queue. The function iterates through this list and checks if any of the events are of type
        "QUIT", which indicates that the user has requested to close the Pygame window. If such an event
        is found
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        """
        This function updates the game loop, handles events, updates the active scene, and changes
        scenes based on game status.
        """
        while self.loop:
            self.fps.tick(60)
            self.activeScene = None
            for scene in self.scenes:
                if not scene.change_scene:
                    self.activeScene = scene
                    break

            if not self.activeScene:
                self.loop = False
                continue

            events = pygame.event.get()
            self.globalEvents(events)
            self.activeScene.events(events, self.game)
            gameStatus = self.activeScene.update(self.game)
            self.activeScene.draw(self.window)

            if gameStatus == 'win':
                self.scenes = [Scene6()]

            if gameStatus == 'loss':
                self.scenes = [Scene7()]

            pygame.display.update()
