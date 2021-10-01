import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("pygame")

image_bg = pygame.image.load("image/qorud.svg")
image_fish = pygame.image.load("image/fish.svg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_fish_width = image_fish.get_rect().size[0]
size_fish_height = image_fish.get_rect().size[1]

x_pos_fish = size_bg_width/2 - size_fish_width/2
y_pos_fish = 180

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    background.blit(image_bg, (-9,-7))
    background.blit(image_fish, (x_pos_fish, y_pos_fish))
    pygame.display.update()

pygame.quit()

