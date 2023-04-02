from window import Window
from scene1 import Scene1
from scene2 import Scene2

class Game:

    def __init__(self, size, name):
        self.scenes = [Scene1(), Scene1()]
        self.window = Window(size, name, self.scenes)

    def start(self):
        self.window.update()