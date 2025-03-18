# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from  player import player
from constants import *


print("Starting Asteroids!")

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

pygame.init
clock = pygame.time.Clock()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
player.containers = (updatable, drawable)

player1 = player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

print("Number of objects in updatable:", len(updatable))
print("Number of objects in drawable:", len(drawable))

def main():
    dt = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill((0,0,0))

        
        updatable.update(dt)
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()


        clock.tick(60)
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

