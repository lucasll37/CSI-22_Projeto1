import moviepy.editor
import pygame
from obj import Obj


class Scene6:

    def __init__(self):

        # self.background = Obj("gameover", 1, None, 0, 0)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = []
        # self.list_group = [self.background]
        self.video = moviepy.editor.VideoFileClip("./assets/final_0.mp4")

    def update(self, game):

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/ending_theme_ohio-59.mp3")
            pygame.mixer.music.play(-1)
            self.video.preview()
            self.justBegin = False

        if self.time > 4800:
            self.change_scene = True

        self.time += 1

    def events(self, events, game):
        for event in events:
            pass

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
