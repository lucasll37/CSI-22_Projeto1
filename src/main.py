# This code is importing the `Game` class from a module called `game`,
# creating an instance of the `Game` class with a specified size and name, and
# then starting the game. The `Game` class likely contains the main game loop
# and handles game logic and rendering.
from game import Game

size = [1280, 720]
name = "Ohio-59"

game = Game(size, name)
game.start()
