# This is a class for a game over scene in a Pygame game, which displays a background image and plays
# a music track until a certain time has elapsed.
import pygame

from obj import Obj


class Scene7:

    def __init__(self):
        """
        This is the initialization function for a game over screen with a background object and some
        variables.
        """

        self.background = Obj("gameover", 1, None, 0, 0)
        self.change_scene = False
        self.main = False
        self.justBegin = True
        self.time = 0
        self.list_group = [self.background]

    def update(self, game):
        """
        This function updates the game state and checks if it's time to change the scene.

        :param game: The "game" parameter is likely an instance of the main game class or module that
        this update function is a part of. It is used to access and modify game state and objects
        """

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/game_over_theme_ohio-59.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

        if self.time > 2000:
            self.change_scene = True

        self.time += 1

    def events(self, events, game):
        """
        This is a skeleton function that takes in a list of events and a game object, but currently does
        nothing with them.

        :param events: This parameter is a list of events that have occurred in the game. Each event is
        represented as an object or dictionary containing information about the event, such as the type
        of event, the player or object involved, and any additional data related to the event
        :param game: The "game" parameter is likely an instance of a game object or class that the
        function is being called on. It may contain information about the current state of the game,
        such as the player's score, the level they are on, or the objects currently on the screen. The
        function may use
        """
        for event in events:
            pass

    def draw(self, window):
        """
        This function draws the groups in a window and animates them if they have a time frame.

        :param window: The "window" parameter is likely a reference to the game window or screen where
        the game graphics will be displayed. The "draw" method is likely responsible for rendering the
        game objects onto this window
        """
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
