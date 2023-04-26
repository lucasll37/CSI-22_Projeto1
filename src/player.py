import pygame
from obj import Obj

class Player(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.killed = False
        self.aux = True
        self.soundCollision = pygame.mixer.Sound("sounds/bomba.mp3")

    def collision(self, group):
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.killed = True
            self.soundCollision.play()

    def flipRight(self):
        self.imageBase = self.imageAux + '_R'
        if not self.aux:
            self.sprite.rect[0] -= 0
            self.aux = True

    def flipLeft(self):
        self.imageBase = self.imageAux
        if self.aux:
            self.sprite.rect[0] += 0
            self.aux = False


