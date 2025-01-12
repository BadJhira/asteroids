# this allows us to use code from the open-source library throughout the file
import pygame # type: ignore
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH * 0.5, SCREEN_HEIGHT * 0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(pygame.Color(0,0,0))
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) * 0.001

if __name__ == "__main__":
    main()