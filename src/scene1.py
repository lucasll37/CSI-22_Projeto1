# This is a class for the first scene of a game, which includes moving backgrounds, bullets, and a
# plane, as well as collision detection and event handling.
import random

import pygame

from obj import Obj
from plane import Plane


class Scene1:

    def __init__(self):
        """
        This function initializes various objects and variables for a game scene in Python.
        """
        self.background1 = Obj("background", 1, None, 0, 0)
        self.background2 = Obj("background", 1, None, 1280, 0)
        self.plane = Plane("plane", 1, None, 100, random.randrange(9, 400))
        self.bullet1 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet2 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet3 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet4 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet5 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet6 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet7 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet8 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet9 = Obj("bullet", 5, 20, 1280, 620)
        self.bullet10 = Obj("bullet", 5, 20, 1280, 620)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.list_group = [
            self.background1,
            self.background2,
            self.plane,
            self.bullet1,
            self.bullet2,
            self.bullet3,
            self.bullet4,
            self.bullet5,
            self.bullet6,
            self.bullet7,
            self.bullet8,
            self.bullet9,
            self.bullet10
        ]

        self.speedMovePlane = 10
        self.speedPlane = 5
        self.speedBullet = 1
        self.planeMoveUp = False
        self.planeMoveDown = False
        self.soundMeme = pygame.mixer.Sound("sounds/euvoucair.mp3")

    def moveBackground(self):
        """
        This function moves two background sprites horizontally and resets their positions when one of
        them goes off-screen.
        """
        self.background1.sprite.rect[0] -= self.speedPlane
        self.background2.sprite.rect[0] -= self.speedPlane
        if self.background1.sprite.rect[0] < -1280:
            self.background1.sprite.rect[0] = 0
            self.background2.sprite.rect[0] = 1280

    def moveBullets(self):
        """
        This function moves 10 bullets on the screen and kills them if they go off the screen.
        """
        temp = 10
        self.bullet1.sprite.rect[0] -= temp * self.speedBullet
        self.bullet1.sprite.rect[1] -= 1 * self.speedBullet
        self.bullet2.sprite.rect[0] -= temp * self.speedBullet
        self.bullet2.sprite.rect[1] -= 2 * self.speedBullet
        self.bullet3.sprite.rect[0] -= temp * self.speedBullet
        self.bullet3.sprite.rect[1] -= 3 * self.speedBullet
        self.bullet4.sprite.rect[0] -= temp * self.speedBullet
        self.bullet4.sprite.rect[1] -= 4 * self.speedBullet
        self.bullet5.sprite.rect[0] -= temp * self.speedBullet
        self.bullet5.sprite.rect[1] -= 5 * self.speedBullet
        self.bullet6.sprite.rect[0] -= temp * self.speedBullet
        self.bullet6.sprite.rect[1] -= 6 * self.speedBullet
        self.bullet7.sprite.rect[0] -= temp * self.speedBullet
        self.bullet7.sprite.rect[1] -= 7 * self.speedBullet
        self.bullet8.sprite.rect[0] -= temp * self.speedBullet
        self.bullet8.sprite.rect[1] -= 8 * self.speedBullet
        self.bullet9.sprite.rect[0] -= temp * self.speedBullet
        self.bullet9.sprite.rect[1] -= 9 * self.speedBullet
        self.bullet10.sprite.rect[0] -= temp * self.speedBullet
        self.bullet10.sprite.rect[1] -= 10 * self.speedBullet

        if self.bullet1.sprite.rect[0] < -100:
            self.bullet1.sprite.kill()
            self.bullet2.sprite.kill()
            self.bullet3.sprite.kill()
            self.bullet4.sprite.kill()
            self.bullet5.sprite.kill()
            self.bullet6.sprite.kill()
            self.bullet7.sprite.kill()
            self.bullet8.sprite.kill()
            self.bullet9.sprite.kill()
            self.bullet10.sprite.kill()

    def movePlane(self):
        """
        The function moves a plane sprite up or down within certain boundaries based on user input.
        """
        if not self.plane.crash:
            if self.planeMoveUp:
                self.plane.sprite.rect[1] -= self.speedMovePlane
                if self.plane.sprite.rect[1] < 9:
                    self.plane.sprite.rect[1] = 9

            elif self.planeMoveDown:
                self.plane.sprite.rect[1] += self.speedMovePlane
                if self.plane.sprite.rect[1] > 400:
                    self.plane.sprite.rect[1] = 400

    def movePlaneEvent(self, event):
        """
        This function handles keyboard events for moving a plane up or down in a Pygame game.

        :param event: This parameter represents a Pygame event object, which contains information about
        a user input or system event that has occurred, such as a key press or mouse movement. The
        function is designed to handle events related to moving a plane in a game, and it checks whether
        the event is a key press or key
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.planeMoveUp = True

            elif event.key == pygame.K_DOWN:
                self.planeMoveDown = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.planeMoveUp = False

            elif event.key == pygame.K_DOWN:
                self.planeMoveDown = False

    def update(self, game):
        """
        This function updates the game by moving the background, bullets, and plane, checking for
        collisions, and playing sounds.

        :param game: The game object that contains all the necessary information and functions for the
        game to run. It is likely an instance of a class that manages the game loop, updates the game
        state, and renders the game graphics
        """
        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/plane.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

        self.moveBackground()
        if self.time > 500:
            self.moveBullets()

        if self.time > 1100:
            self.change_scene = True

        self.movePlane()

        self.plane.collision(self.bullet1.group)
        self.plane.collision(self.bullet2.group)
        self.plane.collision(self.bullet3.group)
        self.plane.collision(self.bullet4.group)
        self.plane.collision(self.bullet5.group)
        self.plane.collision(self.bullet6.group)
        self.plane.collision(self.bullet7.group)
        self.plane.collision(self.bullet8.group)
        self.plane.collision(self.bullet9.group)
        self.plane.collision(self.bullet10.group)

        if self.time == 1000:
            self.soundMeme.play()

        self.time += 1

    def events(self, events, game):
        """
        This function takes in a list of events and a game object, and for each event in the list, it
        calls the movePlaneEvent method with the event as an argument.

        :param events: A list of events that have occurred in the game, such as user input or system
        events
        :param game: The "game" parameter is likely an instance of a game engine or framework that is
        being used to create the game. It could contain various properties and methods related to the
        game, such as the game window, game state, game objects, and so on. The "events" parameter is
        likely a
        """
        for event in events:
            self.movePlaneEvent(event)

    def draw(self, window):
        """
        This function draws the groups in a list on a given window, and if a group has a time frame, it
        animates the group.

        :param window: The "window" parameter is likely a reference to the game window or screen where
        the game graphics will be drawn. It is probably an object of a graphics library such as Pygame
        or Pyglet. The "draw" method is likely used to draw the game objects onto the window
        """
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
