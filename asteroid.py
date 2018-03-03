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
        for i in range(10):
            self.points.append(r + random.randint(-r//2, r//2))

    def draw(self, screen):
        pointsNow = []
        for i in range(10):
            angle = mapFromTo(i, 0, 10, 0, math.pi * 2)
            coor = (polarToCart(angle, self.points[i]))
            pointsNow.append((coor.x + self.x, coor.y + self.y))
        self.rect = pygame.draw.aalines(screen, self.color, True, pointsNow)
