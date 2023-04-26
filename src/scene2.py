
# This is a class for Scene2 that updates, handles events, and draws objects in a game window.
from obj import Obj


class Scene2:

    def __init__(self):
        """
        This is the initialization function for a class that sets up variables including a background
        object, a change_scene flag, a time variable, and a list of groups.
        """
        self.background = Obj("ejeta", 1, None, 0, 0)
        self.change_scene = False
        self.time = 0
        self.list_group = [self.background]

    def update(self, game):
        """
        This function updates the game and changes the scene if the time is greater than 200.

        :param game: It is likely that "game" is an instance of a game class or module that contains the
        main game loop and other game-related functions and variables. The "update" function is likely a
        method of a game object or scene that is called every frame to update the state of the game
        """
        if self.time > 200:
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
