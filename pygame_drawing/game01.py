import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("pygame")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    background.fill((255, 255, 255))
    # pygame.draw.line(background, (0,0,0), (240,0), (240,360))
    # pygame.draw.line(background, (0,0,0), (0,180), (480,180))

    for i in range(0,480,240):
        pygame.draw.line(background, (0,0,0), (i, 0), (i, 360))
    
    # pygame.draw.circle(background, (0,0,0), (120,90), 50)
    # pygame.draw.circle(background, (0,0,0), (120,90), 50, 5)
    
    # pygame.draw.rect(background, (0,0,0), (240, 180, 50, 50))
    # pygame.draw.rect(background, (0,0,0), (240, 180, 50, 50), 5)
    
    # pygame.draw.ellipse(background, (0,0,0), (360, 30, 50, 50))
    # pygame.draw.ellipse(background, (0,0,0), (360, 30, 50, 50), 5)
    
    # pygame.draw.polygon(background, (0,0,0), [[100,100], [0,200], [200,200]])
    # pygame.draw.polygon(background, (0,0,0), [[100,100], [0,200], [200,200]], 5)
    # pygame.draw.polygon(background, (0,0,0), ((146, 0), (291, 106), (236,277), (56, 277), (0, 106)))
    # pygame.draw.polygon(background, (0,0,0), ((146, 0), (291, 106), (236,277), (56, 277), (0, 106)), 5)

    pygame.display.update()

pygame.quit()