import pygame

class Window:
    
    def __init__(self, size, name, scenes):
        pygame.init()
        self.window = pygame.display.set_mode(size)
        self.title = pygame.display.set_caption(name)
        self.scenes = scenes
        self.activeScene = None
        self.loop = True

    def globalEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.loop = False
            
    def update(self):
        while self.loop:

            for scene in self.scenes:
                if not scene.change_scene:
                    self.activeScene = scene
                    break

                self.loop = False

            events = pygame.event.get()
            self.globalEvents(events)
            self.activeScene.events(events)
            self.activeScene.update()
            self.activeScene.draw(self.window)

            pygame.display.update()