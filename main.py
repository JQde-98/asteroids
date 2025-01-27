import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot

def main():

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = (SCREEN_WIDTH / 2)
    y = (SCREEN_HEIGHT / 2)

    player = Player(x, y, PLAYER_RADIUS)
    field = AsteroidField()

    ### Game-loop below###
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        dt = (clock.tick(60)) / 1000
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if i.collision(player):
                print("Game Over!")
                exit()
        for i in drawable:
            i.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()