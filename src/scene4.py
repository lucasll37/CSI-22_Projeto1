# The Scene4 class defines the fourth scene of a game, including the background, player, clouds, and
# bullets, and handles their movement and collision detection.
import random

import pygame

from cloud import Cloud
from obj import Obj
from player import Player


class Scene4:

    def __init__(self):
        """
        This function initializes various game objects and settings for a game.
        """
        self.background = Obj("sky", 1, None, 0, 0)
        self.parachute = Player("parachute", 1, None, 570, 10)
        self.player = Player("tile", 20, 3, 600, 190)
        self.cloud1 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
        self.cloud2 = None
        self.shoot1 = Obj("fire", 1, None, random.randrange(0, 1000), 720)
        self.shoot2 = Obj("fire", 1, None, random.randrange(0, 1000), 720)
        self.shoot3 = Obj("fire", 1, None, random.randrange(0, 1000), 720)
        self.shoot4 = Obj("fire", 1, None, random.randrange(0, 1000), 720)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.offsetTimeCloud = 130
        self.speedFall = 3
        self.speedMovePlayer = 6
        self.speedShot = 6
        self.fireXDirectionModRange = 5
        self.timeClimaxGame = 4400
        self.fireXDirection = random.randrange(
            -self.fireXDirectionModRange, self.fireXDirectionModRange)
        self.playerMoveLeft = False
        self.playerMoveRight = False
        self.createFire = True

        self.list_group = [self.background, self.cloud1,
                           self.parachute,
                           self.player,
                           self.shoot1, self.shoot2, self.shoot3, self.shoot4]

    def moveCloud(self):
        """
        This function moves two cloud sprites upwards by a specified speed.
        """
        self.cloud1.sprite.rect[1] -= self.speedFall
        if self.cloud2:
            self.cloud2.sprite.rect[1] -= self.speedFall

    def movePlayer(self):
        """
        This function moves the player and their parachute sprite left or right based on user input,
        within certain boundaries.
        """
        if self.playerMoveLeft:
            if self.player.sprite.rect[0] > 5:
                self.player.sprite.rect[0] -= self.speedMovePlayer
                self.parachute.sprite.rect[0] -= self.speedMovePlayer

        elif self.playerMoveRight:
            if self.player.sprite.rect[0] < 1165:
                self.player.sprite.rect[0] += self.speedMovePlayer
                self.parachute.sprite.rect[0] += self.speedMovePlayer

    def moveBullet(self):
        """
        This function moves four bullets in a random x-direction and a constant y-direction.
        """
        self.shoot1.sprite.rect[1] -= self.speedShot
        self.shoot2.sprite.rect[1] -= self.speedShot
        self.shoot3.sprite.rect[1] -= self.speedShot
        self.shoot4.sprite.rect[1] -= self.speedShot
        self.shoot1.sprite.rect[0] -= random.randrange(-5, 5) + \
            self.fireXDirection
        self.shoot2.sprite.rect[0] -= random.randrange(-5, 5) + \
            self.fireXDirection
        self.shoot3.sprite.rect[0] -= random.randrange(-5, 5) + \
            self.fireXDirection
        self.shoot4.sprite.rect[0] -= random.randrange(-5, 5) + \
            self.fireXDirection

    def movePlayerEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.flipLeft()
                self.playerMoveLeft = True

            elif event.key == pygame.K_RIGHT:
                self.player.flipRight()
                self.playerMoveRight = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.playerMoveLeft = False

            elif event.key == pygame.K_RIGHT:
                self.playerMoveRight = False

    def update(self, game):
        if self.time % 600 == 0:
            self.speedFall += 1
            self.speedMovePlayer += 2.5
            self.speedShot += 0.7

        if self.time == self.offsetTimeCloud:
            self.cloud2 = Cloud(
                "cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1,
                               self.cloud2, self.parachute,
                               self.player, self.shoot1,
                               self.shoot2, self.shoot3,
                               self.shoot3]

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/ohio-59.mp3")
            pygame.mixer.music.play(1)
            self.justBegin = False

        if self.cloud1.sprite.rect[1] < -200:
            self.cloud1.sprite.kill()
            self.cloud1 = Cloud(
                "cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1,
                               self.cloud2,
                               self.parachute,
                               self.player, self.shoot1,
                               self.shoot2, self.shoot3,
                               self.shoot4]

        if self.cloud2 and self.cloud2.sprite.rect[1] < -200:
            self.cloud2.sprite.kill()
            self.cloud2 = Cloud(
                "cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1,
                               self.cloud2, self.parachute,
                               self.player, self.shoot1, self.shoot2,
                               self.shoot3, self.shoot4]

        # The above code is checking if the "createFire" flag is set to true and if so, it is creating
        # and updating four instances of "fire" objects (shoot1, shoot2, shoot3, shoot4) with random
        # x-coordinates and a fixed y-coordinate of 720. It is also checking if the time elapsed in
        # the game is greater than certain thresholds and if so, it is killing the previous instance
        # of the fire object and creating a new one with a new random x-coordinate. It is also
        # updating the list of sprite groups to include the new instances of the fire object.
        if self.createFire:
            if self.shoot1.sprite.rect[1] < -100:
                self.shoot1.sprite.kill()
                self.shoot1 = Obj(
                    "fire", 1, None, random.randrange(0, 1000), 720)
                self.fireXDirection = random.randrange(
                    -self.fireXDirectionModRange, self.fireXDirectionModRange)
                if self.cloud2:
                    self.list_group = [self.background, self.cloud1,
                                       self.cloud2, self.parachute,
                                       self.player, self.shoot1,
                                       self.shoot2, self.shoot3,
                                       self.shoot4]
                else:
                    self.list_group = [
                        self.background, self.cloud1, self.parachute,
                        self.player, self.shoot1, self.shoot2]
            if (self.shoot2.sprite.rect[1] < -100 and
                    self.time > self.timeClimaxGame/2):
                self.shoot2.sprite.kill()
                self.shoot2 = Obj(
                    "fire", 1, None, random.randrange(0, 1000), 720)
                self.fireXDirection = random.randrange(
                    -self.fireXDirectionModRange, self.fireXDirectionModRange)
                if self.cloud2:
                    self.list_group = [self.background, self.cloud1,
                                       self.cloud2, self.parachute,
                                       self.player, self.shoot1,
                                       self.shoot2, self.shoot3,
                                       self.shoot4]
                else:
                    self.list_group = [
                        self.background, self.cloud1, self.parachute,
                        self.player, self.shoot1,
                        self.shoot2, self.shoot3,
                        self.shoot4]
            if (self.shoot3.sprite.rect[1] < -100 and
                    self.time > 3*self.timeClimaxGame/4):
                self.shoot3.sprite.kill()
                self.shoot3 = Obj(
                    "fire", 1, None, random.randrange(0, 1000), 720)
                self.fireXDirection = random.randrange(
                    -self.fireXDirectionModRange, self.fireXDirectionModRange)
                if self.cloud2:
                    self.list_group = [self.background, self.cloud1,
                                       self.cloud2, self.parachute,
                                       self.player, self.shoot1,
                                       self.shoot2, self.shoot3,
                                       self.shoot4]
                else:
                    self.list_group = [
                        self.background, self.cloud1, self.parachute,
                        self.player, self.shoot1,
                        self.shoot2, self.shoot3,
                        self.shoot4]
            if (self.shoot4.sprite.rect[1] < -100 and
                    self.time > self.timeClimaxGame/4):
                self.shoot4.sprite.kill()
                self.shoot4 = Obj(
                    "fire", 1, None, random.randrange(0, 1000), 720)
                self.fireXDirection = random.randrange(
                    -self.fireXDirectionModRange, self.fireXDirectionModRange)
                if self.cloud2:
                    self.list_group = [self.background, self.cloud1,
                                       self.cloud2, self.parachute,
                                       self.player, self.shoot1,
                                       self.shoot2, self.shoot3,
                                       self.shoot4]
                else:
                    self.list_group = [
                        self.background, self.cloud1, self.parachute,
                        self.player, self.shoot1,
                        self.shoot2, self.shoot3,
                        self.shoot4]

        # `self.moveCloud()`, `self.movePlayer()`, and `self.moveBullet()` are methods of the `Scene4`
        # class that are called in the `update` method.
        self.moveCloud()
        self.movePlayer()
        self.moveBullet()

        # The above code is calling the `collision` method of the `player` object with the `group`
        # attribute of four different `shoot` objects (`shoot1`, `shoot2`, `shoot3`, and `shoot4`).
        # This suggests that the code is checking for collisions between the player and the bullets
        # fired by the `shoot` objects.
        self.player.collision(self.shoot1.group)
        self.player.collision(self.shoot2.group)
        self.player.collision(self.shoot3.group)
        self.player.collision(self.shoot4.group)

        # The above code is a snippet of code written in Python. It is checking if the current time is
        # greater than the climax time of the game. If it is, then it sets the createFire variable to
        # False and creates a list of game objects based on the presence of clouds. If the time is
        # greater than the climax time plus 200, it sets the change_scene variable to True and returns
        # 'win'. If the player is killed, it sets the change_scene variable to True and returns
        # 'loss'. Finally, it increments the time variable by 1.
        if self.time > self.timeClimaxGame:
            self.createFire = False
            if self.cloud1 and self.cloud2:
                self.list_group = [self.background, self.cloud1,
                                   self.cloud2, self.parachute, self.player]

            elif self.cloud1:
                self.list_group = [self.background,
                                   self.cloud1, self.parachute, self.player]

            elif self.cloud2:
                self.list_group = [self.background,
                                   self.cloud2, self.parachute, self.player]

            if self.time > self.timeClimaxGame + 200:
                self.change_scene = True
                return 'win'

        if self.player.killed:
            self.change_scene = True
            return 'loss'

        self.time += 1

    def events(self, events, game):
        """
        This function takes in a list of events and a game object, and for each event in the list, it
        calls the movePlayerEvent method on the object.
        
        :param events: A list of events that have occurred in the game, such as a player pressing a
        button or a timer running out
        :param game: The "game" parameter is likely an instance of a game object or class that contains
        information about the current state of the game, such as the player's score, the level they are
        on, and the positions of various objects in the game world. The "events" parameter is likely a
        list of
        """
        for event in events:
            self.movePlayerEvent(event)

    def draw(self, window):
        """
        This function draws the groups in a window and animates them if they have a time frame.
        
        :param window: The "window" parameter is likely a reference to the game window or screen where
        the game graphics will be displayed. The "draw" method is likely responsible for rendering the
        game objects onto this window
        """
        for group in self.list_group:
            if group.timeFrame:
                group.animation()

            group.group.draw(window)
