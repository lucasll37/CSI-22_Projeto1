# The Cloud class is a subclass of the Obj class that initializes a cloud
# object with a random range from a set of images.
import random

import pygame

from obj import Obj


class Cloud(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        """
        This function initializes a sprite with a image from a 
        specified folder.

        :param imageBase: The base name of the image file without the file
        extension. For example, if the image file is named "cat.png", the
        imageBase would be "cat"
        :param frames: The number of frames in the animation sequence
        :param timeFrame: The timeFrame parameter is the amount of time
        (in seconds) that each frame of the animation should be displayed for
        :param x: The x-coordinate of the sprite's initial position
        on the screen
        :param y: The parameter "y" in the given code is the vertical position
        of the sprite on the screen. It determines the y-coordinate of the 
        top-left corner of the sprite's image
        """
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.sprite.image = pygame.image.load(
            f"assets/{self.imageBase}_{random.randrange(1, 12)}.png")
