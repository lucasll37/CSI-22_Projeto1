import pygame
from obj import Obj

class Plane(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.crash = False

    def collision(self, group):
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.crash = True
            self.imageBase = "planecrash"
            self.sprite.image = pygame.image.load(f"assets/{self.imageBase}_{self.currentFrame}.png")
