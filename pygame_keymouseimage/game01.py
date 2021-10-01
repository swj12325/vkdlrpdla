import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("pygame")

fps = pygame.time.Clock()

image_bg = pygame.image.load("image/qorud.svg")
image_fish = pygame.image.load("image/fish.svg")

size_bg_width = background.get_size()[0]
size_bg_height = background.get_size()[1]

size_fish_width = image_fish.get_rect().size[0]
size_fish_height = image_fish.get_rect().size[1]

x_pos_fish = size_bg_width/2 - size_fish_width/2
y_pos_fish = size_bg_height - size_fish_height

to_x = 0
to_y = 0

play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y = -2
            if event.key == pygame.K_DOWN:
                to_y = 2
            if event.key == pygame.K_RIGHT:
                to_x = 2
            if event.key == pygame.K_LEFT:
                to_x = -2
        if event.type == pygame.KEYUP:
            to_x = 0
            to_y = 0

    x_pos_fish += to_x
    y_pos_fish += to_y

    background.blit(image_bg, (-8,-7))
    background.blit(image_fish, (x_pos_fish, y_pos_fish))
    pygame.display.update()

pygame.quit()