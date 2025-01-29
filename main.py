import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from circleshape import CircleShape
from shot import Shot

def main():

    pygame.init()
    pygame.font.init()

    #game clock and delta time
    clock = pygame.time.Clock()
    dt = 0

    #containers
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #assign classes to groups(containers)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable, drawable, shots)

    #start message
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #setup screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #This block deals with the Score box
    score = 0
    rect_x = 1070
    rect_y = 10
    rect_width = 200
    rect_height = 50
    font = pygame.font.SysFont("Arial", 22)
    text_surface = font.render(f"Score: {score:09}", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2))
    pygame.draw.rect(screen, (0, 0, 225), (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(screen, (225, 225, 225), (rect_x, rect_y, rect_width, rect_height), 3)

    #set up starting point for the player and the player class
    x = (SCREEN_WIDTH / 2)
    y = (SCREEN_HEIGHT / 2)
    player = Player(x, y, PLAYER_RADIUS)

    #setup field that spaws asteroids
    field = AsteroidField()

    asteroid_scores = {
        60: 5,   # Large asteroid
        40: 10,  # Medium asteroid
        20: 15   # Small asteroid
    }

    score_timer = 0

    ######################
    ### Game-loop below ###
    ######################
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Clear the screen
        screen.fill((0, 0, 0))

        dt = (clock.tick(60)) / 1000
        for i in updatable:
            i.update(dt)
        for i in asteroids:
            if i.collision(player):
                print("Game Over!")
                print(f"Final score: {score}")
                exit()
            for shot in shots:
                if i.collision(shot):
                    i.split()
                    shot.kill()
                    score += asteroid_scores.get(i.radius, 0)
        for i in drawable:
            i.draw(screen)

        #Reward player for every 3 sec passed
        score_timer += dt
        if score_timer >= 3:
            score += 5
            score_timer -= 3

        # Redraw the score box (background and border)
        pygame.draw.rect(screen, (0, 0, 225), (rect_x, rect_y, rect_width, rect_height))
        pygame.draw.rect(screen, (225, 225, 225), (rect_x, rect_y, rect_width, rect_height), 3)

        # Update and redraw the score text
        text_surface = font.render(f"Score: {score:09}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(rect_x + rect_width / 2, rect_y + rect_height / 2))
        screen.blit(text_surface, text_rect)  # Draw the text on screen

        pygame.display.flip()

if __name__ == "__main__":
    main()