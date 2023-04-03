import pygame
from obj import Obj
import random

class Cloud(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.sprite.image = pygame.image.load(f"assets/{self.imageBase}_{random.randrange(1, 12)}.png")