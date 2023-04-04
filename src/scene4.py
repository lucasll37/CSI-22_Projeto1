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
        self.speedMovePlayer = 7
        self.speedShot = 7
        self.fireXDirectionModRange = 5
        self.fireXDirection = random.randrange(-self.fireXDirectionModRange, self.fireXDirectionModRange)
        self.playerMoveLeft = False
        self.playerMoveRight = False
        self.list_group = [self.background, self.cloud1, self.parachute, self.player, self.shoot]

    def moveCloud(self):
        self.cloud1.sprite.rect[1] -= self.speedFall 
        if self.cloud2:
            self.cloud2.sprite.rect[1] -= self.speedFall

    def movePlayer(self):
        if self.playerMoveLeft:
            self.player.sprite.rect[0] -= self.speedMovePlayer
            self.parachute.sprite.rect[0] -= self.speedMovePlayer
            if self.parachute.sprite.rect[0] < 9:
                self.player.sprite.rect[0] = 9
                self.parachute.sprite.rect[0] = 9

        elif self.playerMoveRight:
            self.player.sprite.rect[0] += self.speedMovePlayer
            self.parachute.sprite.rect[0] += self.speedMovePlayer
            if self.player.sprite.rect[0] > 1050:
                self.player.sprite.rect[0] = 1050
                self.parachute.sprite.rect[0] = 1050

    def moveBullet(self):
        self.shoot.sprite.rect[1] -= self.speedShot
        self.shoot.sprite.rect[0] -= random.randrange(-5, 5) + self.fireXDirection
    
    def movePlayerEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.playerMoveLeft = True
                    
            elif event.key == pygame.K_RIGHT:
                self.playerMoveRight = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.playerMoveLeft = False
                    
            elif event.key == pygame.K_RIGHT:
                self.playerMoveRight = False



    def update(self):
        print(f"parachutes: {self.parachute.sprite.rect[0]}")
        print(f"player: {self.player.sprite.rect[0]}")

        if self.time == self.offsetTimeCloud:
            self.cloud2 = Cloud("cloud", 1, None, random.randrange(0, 1000), 850)
            self.list_group = [self.background, self.cloud1, self.cloud2, self.parachute, self.player, self.shoot]


        if self.justBegin:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sounds/plane.mp3")
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
            
        # if self.time > 300:    
        #     self.change_scene = True

        self.time += 1


    def events(self, events):
        for event in events:
            self.movePlayerEvent(event)

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)
