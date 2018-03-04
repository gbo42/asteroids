import math
import pygame

# colors
GRAY = (51, 51, 51)
WHITE = (255, 255, 255)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def copy(self):
        return Vector(self.x, self.y)

    def norm(self):
        m = math.sqrt(self.x * self.x + self.y * self.y)
        if m != 0:
            self.x /= m
            self.y /= m
        return self

def mapFromTo(x,a,b,c,d):
   y=(x-a)/(b-a)*(d-c)+c
   return y

def polarToCart(tetha, r):
    x = r * math.cos(tetha)
    y = r * math.sin(tetha)
    return Vector(x, y)

def keyDown(ship, bullets, shot):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ship.thrust()
    if keys[pygame.K_RIGHT]:
        ship.rotate(0.05)
    if keys[pygame.K_LEFT]:
        ship.rotate(-0.05)
    if keys[pygame.K_SPACE] and shot:
        bullets.append(ship.shoot())
        return 2
    return 0
