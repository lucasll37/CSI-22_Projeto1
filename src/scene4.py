import pygame
from obj import Obj
from cloud import Cloud
from player import Player
import random

class Scene4:
    
    def __init__(self):
  
        self.background = Obj("sky", 1, None, 0, 0)
        self.parachute = Player("parachute", 1, None, 570, 10)
        self.player = Player("tile", 20, 3, 600, 190)
        self.cloud1 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
        self.cloud2 = None
        self.shoot = Obj("fire", 1, None, random.randrange(0, 1000), 720)
        self.change_scene = False
        self.justBegin = True
        self.time = 0
        self.offsetTimeCloud = 130
        self.speedFall = 3
        self.speedMovePlayer = 6
        self.speedShot = 6
        self.fireXDirectionModRange = 5
        self.timeClimaxGame = 4800
        self.fireXDirection = random.randrange(-self.fireXDirectionModRange, self.fireXDirectionModRange)
        self.playerMoveLeft = False
        self.playerMoveRight = False
        self.createFire = True

        self.list_group = [self.background, self.cloud1, self.parachute, self.player, self.shoot]



    def moveCloud(self):
        self.cloud1.sprite.rect[1] -= self.speedFall 
        if self.cloud2:
            self.cloud2.sprite.rect[1] -= self.speedFall

    def movePlayer(self):
        if self.playerMoveLeft:
            if self.player.sprite.rect[0] > 5:
                self.player.sprite.rect[0] -= self.speedMovePlayer
                self.parachute.sprite.rect[0] -= self.speedMovePlayer


        elif self.playerMoveRight:
            if self.player.sprite.rect[0] < 1165:
                self.player.sprite.rect[0] += self.speedMovePlayer
                self.parachute.sprite.rect[0] += self.speedMovePlayer


    def moveBullet(self):
        self.shoot.sprite.rect[1] -= self.speedShot
        self.shoot.sprite.rect[0] -= random.randrange(-5, 5) + self.fireXDirection
    
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
            self.speedMovePlayer += 1
            self.speedShot += 1

        if self.time == self.offsetTimeCloud:
            self.cloud2 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player, self.shoot]

        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/ohio-59.mp3")
            pygame.mixer.music.play(-1)
            self.justBegin = False

        if self.cloud1.sprite.rect[1] < -200:
            self.cloud1.sprite.kill()
            self.cloud1 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player, self.shoot]

        if self.cloud2 and self.cloud2.sprite.rect[1] < -200:
            self.cloud2.sprite.kill()
            self.cloud2 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player, self.shoot]

        if self.createFire:
            if self.shoot.sprite.rect[1] < -100:
                self.shoot.sprite.kill()
                self.shoot = Obj("fire", 1, None, random.randrange(0, 1000), 720)
                self.fireXDirection = random.randrange(-self.fireXDirectionModRange, self.fireXDirectionModRange)
                if self.cloud2:
                    self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player, self.shoot]
                else:
                    self.list_group = [self.background, self.cloud1, self.parachute, self.player, self.shoot]


        self.moveCloud()
        self.movePlayer()
        self.moveBullet()

        self.player.collision(self.shoot.group)
            
        if self.time > self.timeClimaxGame:
            self.createFire = False
            if self.cloud1 and self.cloud2:
                self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player]

            elif self.cloud1:
                self.list_group = [self.background, self.cloud1, self.parachute, self.player]

            elif self.cloud2:
                self.list_group = [self.background, self.cloud2, self.parachute, self.player]

            if self.time > self.timeClimaxGame + 600:
                self.change_scene = True
                return 'win' 

        if self.player.killed:
            self.change_scene = True
            return 'loss'
            ...

        self.time += 1


    def events(self, events, game):
        for event in events:
            self.movePlayerEvent(event)

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)
