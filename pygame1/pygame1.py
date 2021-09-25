import pygame

pygame.init()

background = pygame.display.set_mode((600, 360))
pygame.display.set_caption("pygame")

fps = pygame.time.Clock()

play = True
create = False
move = 600

while play:
    deltaTime = fps.tick(60)
    background.fill((0,0,0))
    pygame.draw.circle(background, (255,255,255), (120,180), 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False            
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        create = True

    if create:   
        if move >= 0:
            pygame.draw.circle(background, (255,0,0), ((move,180)), 30)
            move -= 5
            pygame.display.update()
        else:
            create = False


pygame.quit()

