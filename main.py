from constants import *
import pygame
from circleshape import *
from player import *

def main():
    pygame.init()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player1 = Player(x, y, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED)

    Clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        Player1.update(dt)
        Player1.draw(screen)
        pygame.display.flip()
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
