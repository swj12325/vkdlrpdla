import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('pygame')

image_bg = pygame.image.load("image/qorud.svg")
image_fish = pygame.image.load("image/fish.svg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_fish_width = image_fish.get_rect().size[0]
size_fish_height = image_fish.get_rect().size[1]

x_pos_fish = size_bg_width/2 - size_fish_width/2
y_pos_fish = 0


play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
                x_pos_mouse, y_pos_mouse = pygame.mouse.get_pos()
                x_pos_fish = x_pos_mouse - size_fish_width/2
                y_pos_fish = y_pos_mouse - size_fish_height/2
    
    background.blit(image_bg, (-8, -7))
    background.blit(image_fish, (x_pos_fish, y_pos_fish))
    pygame.display.update()

pygame.quit()