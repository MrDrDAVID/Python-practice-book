import pygame
import sys

def exercise_12_1_2() :
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Exercise 12- 1&2")

    bg_color = (169,169,169)
    image = pygame.image.load('chapter-12/images/chewbacca.bmp')
    rect = image.get_rect()
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    rect.bottom = screen_rect.bottom

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()

        screen.fill(bg_color)
        screen.blit(image, rect)

        pygame.display.flip()

exercise_12_1_2()