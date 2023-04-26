import pygame
from scene6 import Scene6
from scene7 import Scene7


class Window:

    def __init__(self, game, size, name, scenes):

        self.window = pygame.display.set_mode(size)
        self.title = pygame.display.set_caption(name)
        self.game = game
        self.scenes = scenes
        self.loop = True
        self.fps = pygame.time.Clock()

    def globalEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.fps.tick(60)
            self.activeScene = None
            for scene in self.scenes:
                if not scene.change_scene:
                    self.activeScene = scene
                    break

            if not self.activeScene:
                self.loop = False
                continue

            events = pygame.event.get()
            self.globalEvents(events)
            self.activeScene.events(events, self.game)
            gameStatus = self.activeScene.update(self.game)
            self.activeScene.draw(self.window)

            if gameStatus == 'win':
                self.scenes = [Scene6()]

            if gameStatus == 'loss':
                self.scenes = [Scene7()]

            pygame.display.update()
