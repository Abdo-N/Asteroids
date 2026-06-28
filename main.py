from constants import *
from logger import log_state
from player import Player
import pygame

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True: #Game loop
        log_state() #state logger
        
        for event in pygame.event.get(): #event tracker?
            
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000 #delta time          
        #print(dt)

        #order is extremely important here
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
