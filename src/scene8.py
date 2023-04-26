# The Scene8 class plays a video and allows the user to skip it by pressing the return key.
import moviepy.editor
import pygame


class Scene8:

    def __init__(self):
        """
        This is the initialization function for a class that sets various attributes including a video
        file clip.
        """
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = []
        self.video = moviepy.editor.VideoFileClip("./assets/briefing_0.mp4")

    def update(self, game):
        """
        This function updates the game scene and plays a briefing sound and video at the beginning, and
        changes the scene after 50 seconds.

        :param game: The "game" parameter is likely an instance of the main game class or module that
        this update function is a part of. It is used to access and modify game state and objects within
        the game
        """

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/briefing.mp3")
            pygame.mixer.music.play(1)
            self.video.preview()
            self.justBegin = False

        if self.time > 1500:
            self.change_scene = True

        self.time += 1

    def events(self, events, game):
        """
        This function checks for a specific key press event and sets a flag to change the scene if that
        key is pressed.

        :param events: A list of events that have occurred in the game, such as keyboard or mouse inputs
        :param game: The "game" parameter is likely an instance of the Pygame library's "Game" class or
        a custom game class that has been created by the developer. It is used to access various
        game-related functions and properties, such as the game window, game clock, and game state
        """
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True

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
