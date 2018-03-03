import pygame
from helpers import *
from asteroid import *
from ship import Ship

# base setup
HEIGHT = 500
WIDTH = 500

# pygame setup
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# game objects
done = False
ship = Ship(250, 250, 50, GREEN)
aQnt = 1
shot = True
bullets = []
asteroids = []

while not done:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == pygame.K_UP:
                ship.thrust()
            if event.key == pygame.K_RIGHT:
                ship.rotate(0.1)
            if event.key == pygame.K_LEFT:
                ship.rotate(-0.1)
            if event.key == pygame.K_SPACE and shot:
                shot = False
                bullets.append(ship.shoot())
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shot = True

    if not ship.update(WIDTH, HEIGHT, asteroids):
        ship = Ship(250, 250, 50, GREEN)
        shot = True
        bullets = []
        asteroids = []
        aQnt = 1


    if len(asteroids) == 0:
        aQnt *= 2
        for i in range(aQnt):
            asteroids.append(randomAsteroid(WIDTH, HEIGHT))

    for a in asteroids:
        if not a.update(WIDTH, HEIGHT, bullets):
            if a.degree < 2:
                asteroids.append(a.createChild())
                asteroids.append(a.createChild())
            asteroids.remove(a)

    for b in bullets:
        if not b.update(WIDTH, HEIGHT):
            bullets.remove(b)

    # render
    screen.fill(GRAY)
    ship.draw(screen)
    for b in bullets:
        b.draw(screen)
    for a in asteroids:
        a.draw(screen)
    pygame.display.flip()

pygame.quit()
