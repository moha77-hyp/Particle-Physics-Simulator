import pygame
import sys
from settings import *
from particle import Particle


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Physics Simulator")
    clock = pygame.time.Clock()
    particles = []

    #the main loop
    running = True
    while running:
        #handle the ball
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                #to make one ball
                new_particle = Particle(mouse_x, mouse_y)
                particles.append(new_particle)

        #refresh
        screen.fill(BLACK)

        #calculations
        for particle in particles:
            particle.move()
            particle.draw(screen)

        #render
        pygame.display.flip()
        clock.tick(FPS)

    #exit
    pygame.quit()
    sys.exit()

#run
if __name__ == "__main__":
    main()