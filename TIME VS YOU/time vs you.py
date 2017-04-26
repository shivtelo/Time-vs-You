import pygame
import random


pygame.init()
arr=[0,0,0,0,0,0,0,0,0,0]
white=(255,255,255)
black=[0,0,0]
r=(240,0,0)
g=(0,170,0)
b=(0,0,170)
cy=(0,255,255)
m=(155,0,155)
y=(255,255,0)
c1=(150,100,50)
c5=(150,50,50)
c3=(255,127,255)
c4=(89,89,89)
c6=(255,127,0)
c7=[85,187,118]
c=black
c2=r
rc=r
cset=(b,black)
cset2=(r,g,cy,y,c7,c3,c5,c1,c6)
arrowinfinity=pygame.display.set_mode((1200,600))
pygame.display.set_caption('TIME VS YOU')

fps=1;
p1=0;
prev=1;
count=0;
go=0;
cr=20;
di=0;
tr=True;
gs=1;
clock=pygame.time.Clock()

gameExit=False
pg1=False



font = pygame.font.SysFont('Arial',35)
im=pygame.image.load('arrow_infinity.jpg')
pygame.mixer.music.load("open2.mp3")
def msg(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [600,0])
def msg2(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [600,50])
def msg3(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [600,100])
def msg4(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [200,150])
def msg5(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [200,200])
def msg6(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [200,50])
def msg7(ms,col):
    screen_text=font.render(ms, True, col)
    arrowinfinity.blit(screen_text, [200,100])
def dispim():
    arrowinfinity.blit(im,(50,30))


pygame.mixer.music.play(-1,0.0)

arrowinfinity.fill(c)
pygame.display.update()
msg6("Welcome Friend,Let's race with clock", c2)
msg7("Pick your favourite color(1-9)", c2)
msg4("Press SPACE to continue", y)
pygame.draw.rect(arrowinfinity, white, [200,200,5,100])
pygame.draw.rect(arrowinfinity, white, [200,200,100,5])
pygame.draw.rect(arrowinfinity, white, [300,200,5,105])
pygame.draw.rect(arrowinfinity, white, [200,300,100,5])
for i in [0, 100, 200]:
    for j in [0, 100, 200]:
        pygame.draw.rect(arrowinfinity, cset2[(int((i / 100) + (j / 100) * 3))], [i + 205, j + 205, 95, 95])
pygame.display.update()
while not pg1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            arrowinfinity.fill(c)
            msg6("Welcome Friends,Let's Play", c2)
            msg7("Pick your favourite color(1-9)", c2)
            msg4("Press SPACE to continue", y)
            for i in [0, 100, 200]:
                for j in [0, 100, 200]:
                    pygame.draw.rect(arrowinfinity, cset2[(int((i / 100) + (j / 100) * 3))], [i + 205, j + 205, 95, 95])
            if event.key == pygame.K_SPACE:
                pg1 = True
            elif event.key == pygame.K_KP1:
                rc = cset2[6]
                pygame.draw.rect(arrowinfinity, white, [200, 400, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [200, 400, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [300, 400, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [200, 500, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP2:
                rc = cset2[7]
                pygame.draw.rect(arrowinfinity, white, [300, 400, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [300, 400, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [400, 400, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [300, 500, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP3:
                rc = cset2[8]
                pygame.draw.rect(arrowinfinity, white, [400, 400, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [400, 400, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [500, 400, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [400, 500, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP4:
                rc = cset2[3]
                pygame.draw.rect(arrowinfinity, white, [200, 300, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [200, 300, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [300, 300, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [200, 400, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP5:
                rc = cset2[4]
                pygame.draw.rect(arrowinfinity, white, [300, 300, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [300, 300, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [400, 300, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [300, 400, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP6:
                rc = cset2[5]
                pygame.draw.rect(arrowinfinity, white, [400, 300, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [400, 300, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [500, 300, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [400, 400, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP7:
                rc = cset2[0]
                pygame.draw.rect(arrowinfinity, white, [200, 200, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [200, 200, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [300, 200, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [200, 300, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP8:
                rc = cset2[1]
                pygame.draw.rect(arrowinfinity, white, [300, 200, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [300, 200, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [400, 200, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [300, 300, 100, 5])
                pygame.display.update()
            elif event.key == pygame.K_KP9:
                rc = cset2[2]
                pygame.draw.rect(arrowinfinity, white, [400, 200, 5, 100])
                pygame.draw.rect(arrowinfinity, white, [400, 200, 100, 5])
                pygame.draw.rect(arrowinfinity, white, [500, 200, 5, 105])
                pygame.draw.rect(arrowinfinity, white, [400, 300, 100, 5])
                pygame.display.update()
        if event.type == pygame.QUIT:
            gameExit = True
            pg1 = True
            go = 0


while not gameExit:

    while go==1:
        arrowinfinity.fill(c)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit=True
                    go=0
        if di==0:
            msg6("Final Score "+str(p2),c2)
            msg7("Oops!Time up,Game Over",y)
            msg4("Press 5 to see ad & play game again",y)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit=True
                    go=0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_KP5:
                        di=1
        else:
            dispim()
            msg("Press Space to play again",c2)
            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    go = 0
                    fps = 1
                    p1 = 0
                    prev = 1
                    count = 0
                    cr = 20
                    di = 0
            else:
                pygame.display.update()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP1:
                    arr[1]=1
                elif event.key == pygame.K_KP2:
                    arr[2]=1
                elif event.key == pygame.K_KP3:
                    arr[3]=1
                elif event.key == pygame.K_KP4:
                    arr[4]=1
                elif event.key == pygame.K_KP5:
                    arr[5]=1
                elif event.key == pygame.K_KP6:
                    arr[6]=1
                elif event.key == pygame.K_KP7:
                    arr[7]=1
                elif event.key == pygame.K_KP8:
                    arr[8]=1
                elif event.key == pygame.K_KP9:
                    arr[9]=1
        p1=p1+arr[prev];
        arrowinfinity.fill(c)
        for i in [0,200,400]:
            for j in [0,200,400]:
                if((i+j)/200)%2==0:
                    pygame.draw.rect(arrowinfinity, white, [i,j,200,200])
        rx=random.randrange(0,3);
        ry=random.randrange(0,3);
        pygame.draw.rect(arrowinfinity, rc, [rx*200,ry*200,200,200])
        pygame.display.update()


        if(go==0):
            msg("Score(Keep it high) "+str(p1),c2)
            msg2("Time(Don't Waste it) "+str(30-(count%30)),y)
            msg3("Current Target "+str(int(cr)),y)
            pygame.draw.rect(arrowinfinity, r, [650, 400,(30-(count%30))*3,20])
            pygame.display.update()
        arr=[0,0,0,0,0,0,0,0,0,0]
        count=count+1;
        prev=rx+1+3*(2-ry);
        if((count%30)==0):
            fps+=.3
            if((p1<cr) and go==0):
                p2=p1
                go=1
            cr+=20
        clock.tick(fps)
pygame.quit()
quit()
