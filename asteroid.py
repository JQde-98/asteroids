import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    containers = []

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        for container in self.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255, 255, 255), center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)

            vector1 = self.velocity.rotate(angle)
            vector2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            asteroid1.velocity = (vector1 * 1.2)
            asteroid2.velocity = (vector2 * 1.2)