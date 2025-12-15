from constants import *
import pygame
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from sys import exit

def main():
    pygame.init()
    print(f"Starting Asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astgroup = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (astgroup, updatable, drawable)
    AsteroidField.containers = (updatable)

    Player1 = Player(x, y, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED)
    Asteroidcluster = AsteroidField()

    Clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updatable.update(dt)

        for ast in astgroup:
            if Player1.collision(ast) == True:
                print("Game over!")
                exit()

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = Clock.tick(60)/1000

if __name__ == "__main__":
    main()
