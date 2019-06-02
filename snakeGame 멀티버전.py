# Snake Game
# Import Statements
import pygame,time,random,sys

# Pygame initialisation
check_error=pygame.init()

#Checking For Errors
if(check_error[1]>0):
    print('Had Initialisation Errors exiting......')
    sys.exit(-1)
else:
    print('(+)Pygame Succesfully initialiZed!')
    
# Sound Variables
crash_sound=pygame.mixer.Sound("Collision.wav")
snakebit_sound=pygame.mixer.Sound('snakehiss2.wav')
gameover_sound=pygame.mixer.Sound('gameover.wav')
pygame.mixer.music.load('asd.mp3')

#Background music
pygame.mixer.music.play(-1)

# Game Icon
snake=pygame.image.load('snake.jpg')
pygame.display.set_icon(snake)

# Variable for speed
x=20
    
# Play Surface
play_surface=pygame.display.set_mode((760,460))
pygame.display.set_caption('Snake Game!')

# Game Colors
red=pygame.Color(255,0,0)       #Game Over Message
green=pygame.Color(0,255,0)     #Snack
black=pygame.Color(0,0,0)       #Score
white=pygame.Color(255,255,255) #Background
brown=pygame.Color(165,42,42)   #Food
blue=pygame.Color(0,0,204)      #Background
yellow=pygame.Color(255,255,0)
purple=pygame.Color(128,0,128)

# FPS Controller
fpsController=pygame.time.Clock()

#Important Variables
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]
snakePos1=[50,100]
snakeBody1=[[50,100],[90,50],[80,50]]

foodPos=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodPos1=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodPos2=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodPos3=[random.randrange(1,72)*10,random.randrange(1,46)*10]
foodSpawn=True
foodSpawn1=True
foodSpawn2=True
foodSpawn3=True
direction = 'RIGHT'
changeto = direction
direction1 = 'L'
changeto1 = direction1
score=0

#Game Over function
def gameOver():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(gameover_sound)
    myFont=pygame.font.SysFont('monospace',72)
    goSurface=myFont.render('Game Over!',True,red)
    goReact=goSurface.get_rect()
    goReact.midtop=(370,15)
    play_surface.blit(goSurface,goReact)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()    #pygame Exit
    sys.exit()       #System Exit
    
def showScore(choice=1):
    sFont=pygame.font.SysFont('monospace',30)
    sSurface=sFont.render('Score:'+str(score),True,black)
    sReact=sSurface.get_rect()
    if choice==1:
        sReact.midtop=(80,10)
    else:
        sReact.midtop=(360,100)
    play_surface.blit(sSurface,sReact)
    
    
# Main Logic
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if(event.key==pygame.K_RIGHT or event.key==ord('d') or event.key==ord('D')):
                changeto='RIGHT'
            if(event.key==pygame.K_LEFT or event.key==ord('a') or event.key==ord('A')):
                changeto='LEFT'
            if(event.key==pygame.K_UP or event.key==ord('w') or event.key==ord('W')):
                changeto='UP'
            if(event.key==pygame.K_DOWN or event.key==ord('s') or event.key==ord('S')):
                changeto='DOWN'
            if(event.key==event.key==ord('l') or event.key==ord('L')):
                changeto1='L'
            if(event.key==event.key==ord('j') or event.key==ord('J')):
                changeto1='J'
            if(event.key==event.key==ord('i') or event.key==ord('I')):
                changeto1='I'
            if(event.key==event.key==ord('k') or event.key==ord('K')):
                changeto1='K'
            if(event.key==pygame.K_ESCAPE):
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    # Direction Validation
    if changeto=='RIGHT' and not direction=='LEFT':
        direction='RIGHT'
    if changeto=='LEFT' and not direction=='RIGHT':
        direction='LEFT'
    if changeto=='UP' and not direction=='DOWN':
        direction='UP'
    if changeto=='DOWN' and not direction=='UP':
        direction='DOWN'
    if changeto1=='L' and not direction=='J':
        direction1='L'
    if changeto1=='J' and not direction=='L':
        direction1='J'
    if changeto1=='I' and not direction=='K':
        direction1='I'
    if changeto1=='K' and not direction=='I':
        direction1='K'
    
    # Update Snake Position
    if direction=='RIGHT':
        snakePos[0]+=10
    if direction=='LEFT':
        snakePos[0]-=10
    if direction=='UP':
        snakePos[1]-=10
    if direction=='DOWN':
        snakePos[1]+=10
    if direction1=='L':
        snakePos1[0]+=10
    if direction1=='J':
        snakePos1[0]-=10
    if direction1=='I':
        snakePos1[1]-=10
    if direction1=='K':
        snakePos1[1]+=10
                
    # Snack Body Mechanism
    snakeBody.insert(0,list(snakePos))
    if snakePos[0]==foodPos[0] and snakePos[1]==foodPos[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        x+=1
        score+=1
        foodSpawn=False

    elif snakePos[0]==foodPos1[0] and snakePos[1]==foodPos1[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        x-=1
        score+=1
        foodSpawn1=False

    elif snakePos[0]==foodPos2[0] and snakePos[1]==foodPos2[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        score+=2
        foodSpawn2=False
        
    elif snakePos[0]==foodPos3[0] and snakePos[1]==foodPos3[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        score-=2
        foodSpawn3=False
    else:
        snakeBody.pop()
        snakeBody1.insert(0,list(snakePos1))
    if snakePos1[0]==foodPos[0] and snakePos1[1]==foodPos[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        x+=1
        score+=1
        foodSpawn1=False

    elif snakePos1[0]==foodPos1[0] and snakePos1[1]==foodPos1[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        x-=1
        score+=1
        foodSpawn2=False
        
    elif snakePos1[0]==foodPos2[0] and snakePos1[1]==foodPos2[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        score+=2
        foodSpawn3=False
    elif snakePos1[0]==foodPos3[0] and snakePos1[1]==foodPos3[1]:
        pygame.mixer.Sound.play(snakebit_sound)
        score-=2
        foodSpawn3=False 
    else:
        snakeBody1.pop()
        
    # food Eating
    if foodSpawn == False:
        foodPos = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn = True

    if foodSpawn1 == False:
        foodPos1 = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn1 = True

    if foodSpawn2 == False:
        foodPos2 = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn2 = True

    if foodSpawn3 == False:
        foodPos3 = [random.randrange(1,72)*10,random.randrange(1,46)*10]
    foodSpawn3 = True
    
    #Draw Snake
    play_surface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(play_surface,red, pygame.Rect(pos[0],pos[1],10,10))
    for pos in snakeBody1:
        pygame.draw.rect(play_surface,blue, pygame.Rect(pos[0],pos[1],10,10))
        
    # Draw Food
    pygame.draw.rect(play_surface,yellow, pygame.Rect(foodPos[0],foodPos[1],10,10))
         
    # Draw Food
    pygame.draw.rect(play_surface,green, pygame.Rect(foodPos1[0],foodPos1[1],10,10))

    # Draw Food
    pygame.draw.rect(play_surface,black, pygame.Rect(foodPos2[0],foodPos2[1],10,10))

    # Draw Food
    pygame.draw.rect(play_surface,purple, pygame.Rect(foodPos3[0],foodPos3[1],10,10))
    
    
    
    # Boundry
    if snakePos[0]>750 or snakePos[0]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    if snakePos[1]>450 or snakePos[1]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    if snakePos1[0]>750 or snakePos1[0]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    if snakePos1[1]>450 or snakePos1[1]<0:
        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        gameOver()
    
    # Hitting Itself
    for block in snakeBody[1:]:
        if snakePos[0]==block[0] and snakePos[1]==block[1]:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(crash_sound)
            time.sleep(1)
            gameOver()
        if snakePos1[0]==block[0] and snakePos1[1]==block[1]:
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(crash_sound)
            time.sleep(1)
            gameOver()

    
    showScore()
    pygame.display.flip()
    fpsController.tick(x)


    
