import pygame
from helpers import *
from asteroid import *
from ship import Ship

# base setup
HEIGHT = 600
WIDTH = 800

# pygame setup
pygame.init()
pygame.key.set_repeat(20, 20)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# game objects
done = False
ship = Ship(WIDTH/2, HEIGHT/2, 35, WHITE)
aQnt = 0
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shot = True

    if keyDown(ship, bullets, shot) == 2:
        shot = False

    if not ship.update(WIDTH, HEIGHT, asteroids):
        ship = Ship(WIDTH/2, HEIGHT/2, 35, WHITE)
        shot = True
        bullets = []
        asteroids = []
        aQnt = 0

    if len(asteroids) == 0:
        aQnt += 1
        for i in range(aQnt):
            asteroids.append(randomAsteroid(WIDTH, HEIGHT, ship))

    for a in asteroids:
        if not a.update(WIDTH, HEIGHT, bullets):
            if a.degree < 2:
                asteroids.append(a.createChild(ship))
                asteroids.append(a.createChild(ship))
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
