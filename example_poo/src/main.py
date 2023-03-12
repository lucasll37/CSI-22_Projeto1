from obj import Obj
from window import Window

teste


class Game:
    def __init__(self):
        self.display = Window(1280, 720, "Futebol")
        self.bg = Obj("assets/field.png", 0, 0)
        self.display.add_obj(self.bg.drawing(self.display.window))


Game().display.updates()
