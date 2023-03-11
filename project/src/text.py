import pygame


class Text:
    def __init__(self, size, text):
        self.font = pygame.font.SysFont("Arial bold", size)
        self.render = self.font.render(text, False, (255, 255, 255))

    def draw(self, window, x, y):
        window.blit(self.render, (x, y))

    def update(self, text):
        self.render = self.font.render(text, False, (255, 255, 255))
