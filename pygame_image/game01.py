import pygame

pygame.init()

image_bg = pygame.image.load("image/qorud.svg")
image_fish = pygame.image.load("image/fish.svg")


# list = [0,1,2,3]
# list[0] => 0
# list[3] => 3
# "list" == "background.get_size()"
size_bg_width = image_bg.get_rect().size[0]
size_bg_height = image_bg.get_rect().size[1]
print(size_bg_height,size_bg_width)

background = pygame.display.set_mode((size_bg_width, size_bg_height))
pygame.display.set_caption("pygame")


size_fish_width = image_fish.get_rect().size[0]
size_fish_height = image_fish.get_rect().size[1]

x_pos_fish = size_bg_width/2
y_pos_fish = 180

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    
    background.blit(image_bg, (0,0))
    background.blit(image_fish, (x_pos_fish, y_pos_fish))
    pygame.display.update()

pygame.quit()

