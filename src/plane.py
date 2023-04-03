import pygame
from obj import Obj

class Plane(Obj):

    def __init__(self, imageBase, frames, timeFrame, x, y):
        super().__init__(imageBase, frames, timeFrame, x, y)
        self.crash = False
        self.soundCollision = pygame.mixer.Sound("sounds/bomba.mp3")


    def collision(self, group):
        if pygame.sprite.spritecollide(self.sprite, group, True):
            self.crash = True
            self.imageBase = "planecrash"
            self.soundCollision.play()
            self.sprite.image = pygame.image.load(f"assets/{self.imageBase}_{self.currentFrame}.png")

            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/emg.mp3")
            pygame.mixer.music.play(-1)
