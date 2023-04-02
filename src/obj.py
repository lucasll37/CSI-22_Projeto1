import pygame

class Obj:

    def __init__(self, imageBase, frames, x, y, show = False):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.frames = frames
        self.currentFrame = 0
        self.sprite.image = pygame.image.load(f"{imageBase}_{self.currentFrame}.png")
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y
        self.show = show