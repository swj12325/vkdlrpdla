import pygame

pygame.init()

background = pygame.display.set_mode((600, 360))
pygame.display.set_caption("pygame")

fps = pygame.time.Clock()

play = True
create = True
delete = False
start = True
move = 600

red = (255,0,0)
black = (0,0,0)
color = [red, black]
count = 0

while play:
    deltaTime = fps.tick(60)
    background.fill((0,0,0))
    pygame.draw.circle(background, (255,255,255), (120,180), 30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False               
        
        if event.type == pygame.KEYDOWN:
            if (move > 140 and move < 180) or (move < 100 and move > 60):
                print("miss")
            elif move < 140 and move > 100:
                print("good") 
            create = False
            move = 600
            
        
        if event.type == pygame.KEYUP:
            create = True
        
    if create: 
        if move >= 0:
            count = 0
            pygame.draw.circle(background, color[count], ((move,180)), 30)
            move -= 5
        else:
            move = 600
            create = False
    pygame.display.update()


pygame.quit()

