import pygame
import random

pygame.init()

# num pad
pygameKeyEvent = [
    pygame.K_KP1,
    pygame.K_KP2,
    pygame.K_KP3,
    pygame.K_KP4,
    pygame.K_KP5,
    pygame.K_KP6,
    pygame.K_KP7,
    pygame.K_KP8,
    pygame.K_KP9
]

# To do: Add controls for no num pad systems
pygameKeyEventAlpha = [
    pygame.K_z,
    pygame.K_x,
    pygame.K_c,
    pygame.K_a,
    pygame.K_s,
    pygame.K_d,
    pygame.K_q,
    pygame.K_w,
    pygame.K_e
]

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
white = (255, 255, 255)
black = [0, 0, 0]
r = (240, 0, 0)
g = (0, 170, 0)
b = (0, 0, 170)
cy = (0, 255, 255)
m = (155, 0, 155)
y = (255, 255, 0)
c1 = (150, 100, 50)
c5 = (150, 50, 50)
c3 = (255, 127, 255)
c4 = (89, 89, 89)
c6 = (255, 127, 0)
c7 = [85, 187, 118]
c = black
c2 = r
rc = r
colorSet = (b, black)
colorSet2 = (r, g, cy, y, c7, c3, c5, c1, c6)
arrowInfinity = pygame.display.set_mode((1200, 600))
pygame.display.set_caption('TIME VS YOU')

fps = 1
p1 = 0
prev = 1
count = 0
go = 0
cr = 20
di = 0
tr = True
gs = 1
clock = pygame.time.Clock()

gameExit = False
pg1 = False

font = pygame.font.SysFont('Arial', 35)


im = pygame.image.load('arrow_infinity.jpg')
pygame.mixer.music.load("open2.mp3")


def msg(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [600, 0])


def msg2(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [600, 50])


def msg3(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [600, 100])


def msg4(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [200, 150])


def msg5(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [200, 200])


def msg6(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [200, 50])


def msg7(ms, col):
    screen_text = font.render(ms, True, col)
    arrowInfinity.blit(screen_text, [200, 100])


def display_image():
    arrowInfinity.blit(im, (50, 30))


pygame.mixer.music.play(-1, 0.0)

arrowInfinity.fill(c)
pygame.display.update()
msg6("Welcome Friend,Let's race with clock", c2)
msg7("Pick your favourite color(1-9)", c2)
msg4("Press SPACE to continue", y)
pygame.draw.rect(arrowInfinity, white, [200, 200, 5, 100])
pygame.draw.rect(arrowInfinity, white, [200, 200, 100, 5])
pygame.draw.rect(arrowInfinity, white, [300, 200, 5, 105])
pygame.draw.rect(arrowInfinity, white, [200, 300, 100, 5])
for i in [0, 100, 200]:
    for j in [0, 100, 200]:
        pygame.draw.rect(arrowInfinity, colorSet2[(int((i / 100) + (j / 100) * 3))], [i + 205, j + 205, 95, 95])
pygame.display.update()
while not pg1:
    for eventPG1 in pygame.event.get():
        if eventPG1.type == pygame.KEYDOWN:
            arrowInfinity.fill(c)
            msg6("Welcome Friends,Let's Play", c2)
            msg7("Pick your favourite color(1-9)", c2)
            msg4("Press SPACE to continue", y)
            for i in [0, 100, 200]:
                for j in [0, 100, 200]:
                    coordinateIndex = (int((i / 100) + (j / 100) * 3))
                    sqX = i + 205
                    sqY = j + 205
                    sqWidth = 95
                    pygame.draw.rect(arrowInfinity, colorSet2[coordinateIndex], [sqX, sqY, sqWidth, sqWidth])
            if eventPG1.key == pygame.K_SPACE:
                pg1 = True
            elif eventPG1.key == pygameKeyEvent[0]:
                rc = colorSet2[6]
                pygame.draw.rect(arrowInfinity, white, [200, 400, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [200, 400, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [300, 400, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [200, 500, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[1]:
                rc = colorSet2[7]
                pygame.draw.rect(arrowInfinity, white, [300, 400, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [300, 400, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [400, 400, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [300, 500, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[2]:
                rc = colorSet2[8]
                pygame.draw.rect(arrowInfinity, white, [400, 400, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [400, 400, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [500, 400, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [400, 500, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[3]:
                rc = colorSet2[3]
                pygame.draw.rect(arrowInfinity, white, [200, 300, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [200, 300, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [300, 300, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [200, 400, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[4]:
                rc = colorSet2[4]
                pygame.draw.rect(arrowInfinity, white, [300, 300, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [300, 300, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [400, 300, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [300, 400, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[5]:
                rc = colorSet2[5]
                pygame.draw.rect(arrowInfinity, white, [400, 300, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [400, 300, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [500, 300, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [400, 400, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[6]:
                rc = colorSet2[0]
                pygame.draw.rect(arrowInfinity, white, [200, 200, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [200, 200, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [300, 200, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [200, 300, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[7]:
                rc = colorSet2[1]
                pygame.draw.rect(arrowInfinity, white, [300, 200, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [300, 200, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [400, 200, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [300, 300, 100, 5])
                pygame.display.update()
            elif eventPG1.key == pygameKeyEvent[8]:
                rc = colorSet2[2]
                pygame.draw.rect(arrowInfinity, white, [400, 200, 5, 100])
                pygame.draw.rect(arrowInfinity, white, [400, 200, 100, 5])
                pygame.draw.rect(arrowInfinity, white, [500, 200, 5, 105])
                pygame.draw.rect(arrowInfinity, white, [400, 300, 100, 5])
                pygame.display.update()
        if eventPG1.type == pygame.QUIT:
            gameExit = True
            pg1 = True
            go = 0

while not gameExit:
    p2 = 0
    while go == 1:
        arrowInfinity.fill(c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                go = 0
        if di == 0:
            msg6("Final Score " + str(p2), c2)
            msg7("Oops!Time up,Game Over", y)
            msg4("Press 5 to see ad & play game again", y)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    go = 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygameKeyEvent[4]:
                        di = 1
        else:
            display_image()
            msg("Press Space to play again", c2)
            pygame.display.update()
            for event in pygame.event.get():
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
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygameKeyEvent[0]:
                    arr[1] = 1
                elif event.key == pygameKeyEvent[1]:
                    arr[2] = 1
                elif event.key == pygameKeyEvent[2]:
                    arr[3] = 1
                elif event.key == pygameKeyEvent[3]:
                    arr[4] = 1
                elif event.key == pygameKeyEvent[4]:
                    arr[5] = 1
                elif event.key == pygameKeyEvent[5]:
                    arr[6] = 1
                elif event.key == pygameKeyEvent[6]:
                    arr[7] = 1
                elif event.key == pygameKeyEvent[7]:
                    arr[8] = 1
                elif event.key == pygameKeyEvent[8]:
                    arr[9] = 1
        p1 = p1 + arr[prev]
        arrowInfinity.fill(c)
        for i in [0, 200, 400]:
            for j in [0, 200, 400]:
                if ((i + j) / 200) % 2 == 0:
                    pygame.draw.rect(arrowInfinity, white, [i, j, 200, 200])
        rx = random.randrange(0, 3)
        ry = random.randrange(0, 3)
        pygame.draw.rect(arrowInfinity, rc, [rx * 200, ry * 200, 200, 200])
        pygame.display.update()

        if go == 0:
            msg("Score(Keep it high) " + str(p1), c2)
            msg2("Time(Don't Waste it) " + str(30 - (count % 30)), y)
            msg3("Current Target " + str(int(cr)), y)
            pygame.draw.rect(arrowInfinity, r, [650, 400, (30 - (count % 30)) * 3, 20])
            pygame.display.update()
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        count = count + 1
        prev = rx + 1 + 3 * (2 - ry)
        if (count % 30) == 0:
            fps += .3
            if (p1 < cr) and go == 0:
                p2 = p1
                go = 1
            cr += 20
        clock.tick(fps)
pygame.quit()
quit()
