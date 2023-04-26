# This is a class for the first scene of a game, which includes a background image and handles events
# such as pressing the enter key to change scenes.
import pygame

from obj import Obj


class Scene0:

    def __init__(self):
        """
        This is the initialization function for a class that sets up a background object and a list of
        objects.
        """
        self.background = Obj("intro2", 1, None, 0, 0)
        self.change_scene = False
        self.list_group = [self.background]
        self.justBegin = True

    def update(self, game):
        """
        This function updates the game by stopping the current music and playing the intro music if it's
        the beginning of the game.

        :param game: It is likely that "game" is an instance of a class that represents the current
        state of the game being played. The "update" method is probably a method of another class that
        is responsible for updating the game state based on user input or other events. The "update"
        method may be called
        """
        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/intro.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

    def events(self, events, game):
        """
        This function checks for a specific key press event and sets a flag to change the scene if that
        key is pressed.

        :param events: A list of events that have occurred in the game, such as keyboard or mouse inputs
        :param game: The "game" parameter is likely an instance of the Pygame library's "Game" class,
        which is used to manage the game loop, handle events, and update the game state. It is not
        explicitly used in the code snippet provided, but it may be used elsewhere in the program
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True

    def draw(self, window):
        """
        The function iterates through a list of groups and calls their animation method if they have a
        timeFrame attribute.

        :param window: The "window" parameter is likely a reference to the graphical window or canvas on
        which the animation is being drawn. It is probably an object of a graphics library or framework,
        such as Pygame or Tkinter. The "draw" method is likely part of a class that manages the animation
        and updates
        """
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
