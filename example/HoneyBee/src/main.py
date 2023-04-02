import pygame
from menu import Menu
from window import Game
from gameover import GameOver


class Main:

    def __init__(self, sizex, sizey, title):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/bg.ogg")
        pygame.mixer.music.play(-1) # loop

        self.window = pygame.display.set_mode([sizex, sizey])
        self.title = pygame.display.set_caption(title)

        self.menu = Menu("assets/start.png")
        self.game = Game()
        self.gameover = GameOver("assets/gameover.png")

        self.loop = True
        self.fps = pygame.time.Clock()

    def draw(self):
        self.window.fill([0, 0, 0])

        if not self.menu.change_scene:
            self.menu.draw(self.window)

        elif not self.game.change_scene:
            self.game.draw(self.window)
            self.game.update()

        elif not self.gameover.change_scene:
            self.gameover.draw(self.window)

        else:
            self.menu.change_scene = False
            self.game.change_scene = False
            self.gameover.change_scene = False
            self.game.bee.life = 3
            self.game.bee.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False

            if not self.menu.change_scene:
                self.menu.events(event)

            elif not self.game.change_scene:
                self.game.bee.move_bee(event)

            else:
                self.gameover.events(event)

    def update(self):
        while self.loop:
            self.fps.tick(30)  # quantidade de frames por segundo
            self.draw()
            self.events()
            pygame.display.update()


game = Main(360, 640, "BeeHoney")
game.update()
