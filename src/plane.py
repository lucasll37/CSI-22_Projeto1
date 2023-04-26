# The Plane class is a subclass of the Obj class and includes collision detection and sound effects
# for when the plane crashes.
import pygame

from obj import Obj


class Plane(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        """
        This is a constructor function that initializes attributes for an object, including an image,
        frames, time frame, coordinates, a crash flag, and a collision sound.

        :param imageBase: The base image file name or path for the sprite
        :param frames: The number of frames in the animation of the sprite
        :param timeFrame: The time duration (in seconds) for each frame of the animation
        :param x: The x-coordinate of the object's initial position on the screen
        :param y: The parameter "y" in the given code is the vertical position of the object on the
        screen. It is used to set the initial y-coordinate of the object when it is created
        """
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.crash = False
        self.soundCollision = pygame.mixer.Sound("sounds/bomba.mp3")

    def collision(self, group):
        """
        This function detects collisions between a sprite and a group of sprites, triggers a crash
        animation and sound effect, and stops and replaces the background music.

        :param group: The "group" parameter is a Pygame sprite group that contains the sprites that the
        current sprite can collide with. The "spritecollide" method checks for collisions between the
        current sprite and the sprites in the group. If a collision is detected, the code inside the
        "if" statement is executed
        """
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.crash = True
            self.imageBase = "planecrash"
            self.soundCollision.play()
            self.sprite.image = pygame.image.load(
                f"assets/{self.imageBase}_{self.currentFrame}.png")
            self.soundCatch = pygame.mixer.Sound("sounds/bomba.mp3")

            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/emg.mp3")
            pygame.mixer.music.play(-1)
