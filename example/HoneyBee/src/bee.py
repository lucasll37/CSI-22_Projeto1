from obj import Obj
import pygame


class Bee(Obj):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)

        pygame.mixer.init()
        self.soundCatchFlower = pygame.mixer.Sound("sounds/flower.ogg")
        self.soundCatchSpider = pygame.mixer.Sound("sounds/spyder.ogg")

        self.life = 3
        self.score = 0

    def move_bee(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.sprite.rect[0] = pygame.mouse.get_pos()[0] - 35
            self.sprite.rect[1] = pygame.mouse.get_pos()[1] - 30

    def collision(self, group, name):

        collision = pygame.sprite.spritecollide(self.sprite, group, True)
        if collision and name == "Flower":
            self.score += 1
            self.soundCatchFlower.play()

        elif collision and name == "Spider":
            self.life -= 1
            self.soundCatchSpider.play()
