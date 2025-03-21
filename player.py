from circleshape import CircleShape
from constants import *
from bullet import Shot
import pygame

class player(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = PLAYER_RADIUS
        self.__cooldown = 0
        self.rotation = 0
    
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED*dt

    def update(self, dt):
        self.__cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.__cooldown <= 0:
                self.shoot()
                self.__cooldown = PLAYER_SHOOT_COOLDOWN
            
            
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt



    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), player.triangle(self), 2)
        
    
    def shoot(self):
        print("DEBUG: shooting!")
        proj = Shot(self.position[0], self.position[1], SHOT_RADIUS)
        proj.velocity = pygame.math.Vector2(0,1).rotate(self.rotation)
        proj.velocity *= PLAYER_SHOOT_SPEED