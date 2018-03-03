import math
import random
import pygame

from helpers import *
class Asteroid:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.color = color
        self.points = []
        self.rect = 0
        self.speed = Vector(random.random(), random.random()).norm()
        self.angle = 0
        for i in range(10):
            self.points.append(r + random.randint(-r//2, r//2))

    def update(self, w, h):
        self.angle = (self.angle + 0.01)
        self.x = (self.x + self.speed.x) % w
        self.y = (self.y + self.speed.y) % h

        self.pointsNow = []
        for p in range(10):
            angle = mapFromTo(p, 0, 10, 0, math.pi * 2)
            coor = (polarToCart(angle, self.points[p]))
            x = coor.x * math.cos(self.angle) - coor.y * math.sin(self.angle)
            y = coor.y * math.cos(self.angle) + coor.x * math.sin(self.angle)
            self.pointsNow.append((self.x + x, self.y + y))

    def draw(self, screen):
        self.rect = pygame.draw.aalines(screen, self.color, True, self.pointsNow)
