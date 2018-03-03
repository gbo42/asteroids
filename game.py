import pygame
from asteroid import Asteroid
from ship import Ship

HEIGHT = 500
WIDTH = 500

GRAY = (51, 51, 51)
WHITE = (255, 255, 255)
GREEN  = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
done = False

asteroid = Asteroid(100, 100, 50, WHITE)
ship = Ship(250, 250, 50, GREEN)

pygame.key.set_repeat(20, 20)

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

    ship.move(WIDTH, HEIGHT)

    # render
    screen.fill(GRAY)
    ship.draw(screen)
    asteroid.draw(screen)
    pygame.display.flip()

pygame.quit()
