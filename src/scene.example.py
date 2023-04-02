import pygame
from obj import Obj

############################################################################################
#
# ADICIONAR "SceneN()" na lista armazenada na variável "self.scenes" do arquivo "game.py"
#
############################################################################################

class SceneN:
    
    def __init__(self):
        pass
        # self.background = Obj("assets/free_plane_sprite/png/background", 1, 0, 0, True)
        # self.plane = Obj("assets/free_plane_sprite/png/Plane/plane", 2, 20, 20, True)
        # self.change_scene = False
        # self.list_group = [self.background, self.plane]

    def events(self, events):
        for event in events:
            pass
            # if event == pygame.KEYDOWN:
            #    if event.key == pygame.K_RETURN:
            #        self.change_scene = True

    def update(self):
        pass

    def draw(self, window):
        for group in self.list_group:
            group.group.draw(window)

