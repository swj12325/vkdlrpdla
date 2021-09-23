import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("pygame")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()

