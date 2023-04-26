# The class Obj defines an object with animation capabilities in Pygame.
import pygame


class Obj:

    def __init__(self, imageBase, frames, timeFrame, x, y):
        """
        This function initializes a sprite with a given image, number of 
        frames, time per frame, and position.

        :param imageBase: The base name of the image file(s) used for the 
        sprite animation
        :param frames: The number of frames in the animation
        :param timeFrame: The timeFrame parameter is the amount of time (in milliseconds) 
        that each frame of the animation should be displayed for
        :param x: The x-coordinate of the sprite's initial 
        position on the screen
        :param y: The y-coordinate of the sprite's initial 
        position on the screen
        """
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.imageAux = imageBase
        self.imageBase = imageBase
        self.frames = frames
        self.currentFrame = 0
        self.sprite.image = pygame.image.load(
            f"assets/{self.imageBase}_{self.currentFrame}.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.tick = 0
        self.timeFrame = timeFrame

    def animation(self):
        """
        This function animates a sprite by loading a sequence of images and cycling through them at a
        specified time frame.
        """
        self.tick += 1
        if self.tick >= self.timeFrame:
            self.tick = 0
            self.currentFrame += 1
            if self.currentFrame >= self.frames:
                self.currentFrame = 0

            self.sprite.image = pygame.image.load(
                f"assets/{self.imageBase}_{self.currentFrame}.png")
