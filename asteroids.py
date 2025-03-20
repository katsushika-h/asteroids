from circleshape import CircleShape
import pygame

class Asteroids(CircleShape):
    def __init__(self, x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen)
        pygame.draw.circle(screen, (255,255,255), (self.x,self.y) radius=)
        
