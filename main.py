from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import pygame
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    #we have to instantiate the player after adding class to groups
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True: #Game loop
        log_state() #state logger
        
        for event in pygame.event.get(): #event tracker?
            
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 #delta time          
        #print(dt)

        #order is extremely important here
        screen.fill("black")
        updatable.update(dt)

        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over !")
                sys.exit()


        for item in drawable:
            item.draw(screen)
            
        pygame.display.flip()


if __name__ == "__main__":
    main()
