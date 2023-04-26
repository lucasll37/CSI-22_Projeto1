# This is a class for a player object in a game that can collide with other objects and play a sound
# when it collides.
import pygame

from obj import Obj


class Player(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        """
        This is a constructor function that initializes attributes for an object, including an image,
        frames, time frame, position, a boolean value for whether the object has been killed, and a
        sound effect for collisions.

        :param imageBase: The base image file for the sprite
        :param frames: The "frames" parameter is likely a list of images that make up an animation. Each
        image in the list represents a single frame of the animation. When the animation is played, the
        images are displayed in sequence to create the illusion of movement
        :param timeFrame: The time duration (in seconds) for each frame of the animation
        :param x: The x-coordinate of the object's initial position on the screen
        :param y: The parameter "y" in the __init__ method is the initial y-coordinate of the object
        being created. It is used to set the vertical position of the object on the screen
        """
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.killed = False
        self.soundCollision = pygame.mixer.Sound("sounds/bomba.mp3")

    def collision(self, group):
        """
        This function checks for collisions between the sprite associated with the object and a group of
        sprites, and if a collision occurs, it sets a flag indicating that the object has been killed
        and plays a collision sound.

        :param group: The "group" parameter is a collection of sprites that the current sprite
        (self.sprite) may collide with. The function checks if there is a collision between the current
        sprite and any sprite in the group. If there is a collision, the collided sprite is removed from
        the group (True is passed as
        """
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.killed = True
            self.soundCollision.play()

    # Below, there are two empty functions, in case of necessity whether the implementation requires
    def flipRight(self):
        pass

    def flipLeft(self):
        pass
