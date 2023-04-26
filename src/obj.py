import pygame


class Obj:

    def __init__(self, imageBase, frames, timeFrame, x, y):
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
        self.tick += 1
        if self.tick >= self.timeFrame:
            self.tick = 0
            self.currentFrame += 1
            if self.currentFrame >= self.frames:
                self.currentFrame = 0

            self.sprite.image = pygame.image.load(
                f"assets/{self.imageBase}_{self.currentFrame}.png")
