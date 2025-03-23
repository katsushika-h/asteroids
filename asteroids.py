from circleshape import CircleShape
import pygame
import random
from constants import *

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity *dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            aod = random.uniform(20, 50)
            split_a_velo = self.velocity.rotate(aod)
            split_b_velo = self.velocity.rotate(-aod)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_a = Asteroids(self.position[0], self.position[1], new_radius)
            asteroid_a.velocity = split_a_velo
            print("asteroid a created")

            asteroid_b = Asteroids(self.position[0], self.position[1], new_radius)
            asteroid_b.velocity = split_b_velo


