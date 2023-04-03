import pygame
from obj import Obj
from plane import Plane
import random

class Scene1:
    
    def __init__(self):
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


    def moveBackground(self):
        self.background1.sprite.rect[0] -= self.speedPlane
        self.background2.sprite.rect[0] -= self.speedPlane
        if self.background1.sprite.rect[0] < -1280:
            self.background1.sprite.rect[0] = 0
            self.background2.sprite.rect[0] = 1280

    def moveBullets(self):
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


    def update(self):
        self.moveBackground()
        if self.time > 500:    
            self.moveBullets()

        if self.time > 800:    
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
        self.time += 1


    def events(self, events):
        for event in events:
            self.movePlaneEvent(event)

    def draw(self, window):
        for group in self.list_group:
            if group.timeFrame:
                group.animation()
            
            group.group.draw(window)