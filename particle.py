#importing libs
import pygame
import random
from settings import *


class Particle:

    #this class made for handling the physics calculations to keep the code clean

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = random.randint(5, 10) #smart move to make the diameter random to see different
        self.color = random.choice([BLUE, RED, WHITE])  #for random color
        #also for random speed
        self.vel_x = random.uniform(-5, 5)
        self.vel_y = random.uniform(-5, 5)

    def move(self):

        #to refresh the position
        # the law: the_new_position = old_position + speed

        self.vel_y += GRAVITY
        #friction to slowdown the speed
        self.vel_x *= FRICTION
        self.vel_y *= FRICTION
        #refresh the position
        self.x += self.vel_x
        self.y += self.vel_y
        # to check if the ball hit the wall
        self.check_walls()

    def check_walls(self):
        #handle the hit
        # (X-axis)
        if self.x + self.radius > WIDTH:
            self.x = WIDTH - self.radius
            self.vel_x *= -1  # to revers
        elif self.x - self.radius < 0:
            self.x = self.radius
            self.vel_x *= -1  # to revers

        # (Y-axis)
        if self.y + self.radius > HEIGHT:
            self.y = HEIGHT - self.radius
            self.vel_y *= -1  # reverse
        elif self.y - self.radius < 0:
            self.y = self.radius
            self.vel_y *= -1

    def draw(self, screen):
        #visual on the screen
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)