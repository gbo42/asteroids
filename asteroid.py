import math
import random
import pygame

from helpers import *
class Asteroid:
    def __init__(self, x, y, r, color, degree = 0):
        self.degree = degree
        self.x = x
        self.y = y
        self.color = color
        self.points = []
        self.pointsNow = []
        self.rect = pygame.Rect((x, y, r, r))
        self.speed = Vector(1, 1)
        self.dir = Vector(random.randint(-10, 10), random.randint(-10, 10)).norm()
        self.angle = 0
        for i in range(10):
            self.points.append(r + random.randint(-r//2, r//2))

    def update(self, w, h, bullets):
        for bullet in bullets:
            if self.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
                return False
        self.angle = (self.angle + 0.01)
        self.x = (self.x + self.speed.x * self.dir.x) % w
        self.y = (self.y + self.speed.y * self.dir.y) % h

        self.pointsNow = []
        for p in range(10):
            angle = mapFromTo(p, 0, 10, 0, math.pi * 2)
            coor = (polarToCart(angle, self.points[p]))
            x = coor.x * math.cos(self.angle) - coor.y * math.sin(self.angle)
            y = coor.y * math.cos(self.angle) + coor.x * math.sin(self.angle)
            self.pointsNow.append((self.x + x, self.y + y))

        return True

    def draw(self, screen):
        if len(self.pointsNow) > 1:
            self.rect = pygame.draw.aalines(screen, self.color, True, self.pointsNow)

    def createChild(self):
        child = Asteroid(self.x, self.y, 0, self.color, self.degree+1)
        child.angle = self.angle
        child.points = []
        for p in self.points:
            child.points.append(p/2)
        return child


def randomAsteroid(w, h):
    asteroid = Asteroid(random.randint(0, w), random.randint(0, h), 50, WHITE)
    return asteroid
