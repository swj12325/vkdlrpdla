import pygame

pygame.init()

background = pygame.display.set_mode((600, 360))    
pygame.display.set_caption("pygame")    

fps = pygame.time.Clock()

play = True
create = True
move = 600  #오른쪽에서 다가오는 공의 전체적인 위치 설정

red = (255,0,0)
black = (0,0,0)
color = [red, black]
count = 0 #색을 정하는 

while play:
    deltaTime = fps.tick(60) 
    background.fill((0,0,0)) 
    pygame.draw.circle(background, (255,255,255), (120,180), 30) #왼쪽에 존재하는 하얀 공
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False               
        
        if event.type == pygame.KEYDOWN:    #아무 키나 눌렀을 때 실행
            if (move > 140 and move < 180) or (move < 100 and move > 60):   
                print("miss") #move값이 140 초과 180 미만 혹은 180 미만 60 초과일 때 miss 출력

            elif move < 140 and move > 100:
                print("good") #move값이 140 미만 100 초과일 때 good 출력

            create = False    #create 값이 False로 변함
            move = 600        #create 값이 True였을 때 move가 0 미만이 아니었다면 move가 600으로 초기화 되지 못하기에 KEYDOWN 이벤트에서도 move 초기화를 넣음
            
        if event.type == pygame.KEYUP:  #아무 키를 눌렀다 뗐을 때
            create = True    #create 값이 True로 변함
        
    if create:          #create 값이 True일 때 실행, 오른쪽에서 다가오는 원 생성 
        if move >= 0:   #move값이 0 이상일 때
            count = 0   #count를 0(붉은 색)으로 설정
            pygame.draw.circle(background, ((255, 0, 0)), ((move,180)), 30)  #오른쪽에서 다가오는 원 생성
            move -= 7   #move 값을 -5씩 계속 줄여줘서 왼쪽으로 공이 움직이게 만듦
        else:
            move = 600  #move값이 0 미만 일때, move값을 600으로 초기화 시켜줘서 다시 오른쪽으로 가게 함
    pygame.display.update()


pygame.quit()

