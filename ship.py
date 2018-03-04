import pygame
import math
from helpers import *

class Bullet:
    def __init__(self, x, y, d, color):
        self.x = x
        self.y = y
        self.ticks = pygame.time.get_ticks()
        self.color = color
        self.dir = d.copy()
        self.rect =  pygame.Rect((int(self.x), int(self.y), 3, 3))
    def update(self, w, h):
        if pygame.time.get_ticks() - self.ticks > 2500:
            return False
        self.x = (self.x + self.dir.x * 10) % w
        self.y = (self.y + self.dir.y * 10) % h
        return True

    def draw(self, screen):
        self.rect = pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), 3)

class Ship:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.angle = 0
        self.rect = pygame.Rect((0, 0, 0, 0))
        self.dir = Vector(0, 1)
        self.speed = Vector(0, 0)
        self.color = color
        self.original = [Vector(-r/2, -r/2),
                         Vector(r/2, -r/2),
                         Vector(0, r*5/3-r)]
        self.points = [Vector(0, 0), Vector(0, 0), Vector(0, 0)]

    def rotate(self, angle):
        self.angle = (self.angle + angle)
        cart = polarToCart(self.angle, 0.5)
        self.dir.x = -cart.y
        self.dir.y = cart.x

    def thrust(self):
        x = self.speed.x + self.dir.x
        y = self.speed.y + self.dir.y
        if x*x + y*y < 20:
            self.speed.x = x
            self.speed.y = y

    def update(self, w, h, asteroids):
        for a in asteroids:
            if self.rect.colliderect(a.rect):
                return False
        self.x = (self.x + self.speed.x) % w
        self.y = (self.y + self.speed.y) % h
        self.speed.x *= 0.95
        self.speed.y *= 0.95

        for p in range(3):
            x = self.original[p].x * math.cos(self.angle) - self.original[p].y * math.sin(self.angle)
            y = self.original[p].y * math.cos(self.angle) + self.original[p].x * math.sin(self.angle)
            self.points[p].x = self.x + x
            self.points[p].y = self.y + y

        return True

    def draw(self, screen):
        self.rect = pygame.draw.aalines(screen, self.color, True, [(p.x, p.y) for p in self.points])

    def shoot(self):
        return Bullet(self.points[2].x, self.points[2].y, self.dir, WHITE)
