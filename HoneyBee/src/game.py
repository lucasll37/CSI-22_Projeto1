from obj import Obj
from bee import Bee
from text import Text
import random


class Game:
    def __init__(self):
        self.bg1 = Obj("assets/bg.png", 0, 0)
        self.bg2 = Obj("assets/bg.png", 0, -640)

        self.spider = Obj("assets/spider1.png", random.randrange(0, 300), -50)
        self.flower = Obj("assets/flower1.png", random.randrange(0, 300), -50)
        self.bee = Bee("assets/bee1.png", 150, 600)
        self.scoreboard = Text(160, "0")
        self.lifes = Text(60, "3")
        self.change_scene = False

    def draw(self, window):
        self.bg1.draw(window)
        self.bg2.draw(window)
        self.spider.draw(window)
        self.flower.draw(window)
        self.bee.draw(window)
        self.scoreboard.draw(window, 150, 50)
        self.lifes.draw(window, 50, 50)

    def move_bg(self):
        self.bg1.sprite.rect[1] += 4
        self.bg2.sprite.rect[1] += 4

        if self.bg1.sprite.rect[1] > 640:
            self.bg1.sprite.rect[1] = 0

        if self.bg2.sprite.rect[1] > 0:
            self.bg2.sprite.rect[1] = -640

    def move_spiders(self):
        self.spider.sprite.rect[1] += 10

        if self.spider.sprite.rect[1] > 700:
            self.spider.sprite.kill()
            self.spider = Obj("assets/spider1.png",
                              random.randrange(0, 300), -50)

    def move_flowers(self):
        self.flower.sprite.rect[1] += 6

        if self.flower.sprite.rect[1] > 700:
            self.flower.sprite.kill()
            self.flower = Obj("assets/flower1.png",
                              random.randrange(0, 300), -50)

    def gameover(self):
        if self.bee.life <= 0:
            self.change_scene = True

    def update(self):
        self.move_bg()
        self.spider.anim("spider", 8, 4)
        self.flower.anim("flower", 8, 2)
        self.bee.anim("bee", 2, 4)
        self.move_spiders()
        self.move_flowers()
        self.bee.collision(self.spider.group, "Spider")
        self.bee.collision(self.flower.group, "Flower")
        self.gameover()
        self.scoreboard.update(str(self.bee.score))
        self.lifes.update(str(self.bee.life))
