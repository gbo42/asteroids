import pygame
import math
from helpers import *

class Ship:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.angle = 0
        self.dir = Vector(0, 1)
        self.speed = Vector(0, 0)
        self.color = color
        self.original = [Vector(-r/2, -r/2),
                         Vector(r/2, -r/2),
                         Vector(0, r*5/3-r)]
        self.points = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]

    def rotate(self, angle):
        self.angle = (self.angle + angle)
        cart = polarToCart(self.angle, 1)
        self.dir.x = -cart.y
        self.dir.y = cart.x

    def update(self):
        for p in range(3):
            x = self.original[p].x * math.cos(self.angle) - self.original[p].y * math.sin(self.angle)
            y = self.original[p].y * math.cos(self.angle) + self.original[p].x * math.sin(self.angle)
            self.points[p].x = self.x + x
            self.points[p].y = self.y + y

    def thrust(self):
        self.speed.x = self.speed.x + self.dir.x
        self.speed.y = self.speed.y + self.dir.y

    def move(self, w, h):
        self.x = (self.x + self.speed.x) % w
        self.y = (self.y + self.speed.y) % h
        self.speed.x *= 0.95
        self.speed.y *= 0.95
        self.update()

    def draw(self, screen):
        pygame.draw.aalines(screen, self.color, True, [(p.x, p.y) for p in self.points])
