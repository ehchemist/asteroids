import pygame
from circleshape import *

class Player(CircleShape):
    def __init__(self, x, y, PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.turn_speed = PLAYER_TURN_SPEED
        self.speed = PLAYER_SPEED
         
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += self.turn_speed * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
