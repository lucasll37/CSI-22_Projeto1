# The Scene6 class plays a video clip and music while updating and drawing the scene until a certain
# time is reached.
import moviepy.editor
import pygame


class Scene6:

    def __init__(self):
        """
        The function initializes various variables and loads a video file.
        """

        # self.background = Obj("gameover", 1, None, 0, 0)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = []
        # self.list_group = [self.background]
        self.video = moviepy.editor.VideoFileClip("./assets/final_0.mp4")
        self.clip = self.video.subclip(0, 12)
        self.clip = self.clip.speedx(0.2)

    def update(self, game):
        """
        This function updates the game state and checks if it's time to change the scene.

        :param game: It is a parameter that is being passed to the function "update". It is not clear
        what type of object "game" is, as it is not used in the function. It is possible that it is an
        instance of a game class or module that contains information about the game state
        """

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/ending_theme_ohio-59.mp3")
            pygame.mixer.music.play(-1)
            self.clip.preview()
            self.justBegin = False

        if self.time > 4800:
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
        such as player positions, scores, or game settings. The function may use this information to
        determine how to handle the events passed
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
