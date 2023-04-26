import moviepy.editor
import pygame
from obj import Obj


class Scene8:

    def __init__(self):

        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = []
        # self.list_group = [self.background]
        self.video = moviepy.editor.VideoFileClip("./assets/briefing_0.mp4")

    def update(self, game):

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/briefing.mp3")
            pygame.mixer.music.play(1)
            self.video.preview()
            self.justBegin = False

        if self.time > 1000:
            self.change_scene = True

        self.time += 1

    def events(self, events, game):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.change_scene = True

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
