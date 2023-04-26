import pygame
from obj import Obj


class Player(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.killed = False
        self.soundCollision = pygame.mixer.Sound("sounds/bomba.mp3")

    def collision(self, group):
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.killed = True
            self.soundCollision.play()

    def flipRight(self):
        pass

    def flipLeft(self):
        pass
