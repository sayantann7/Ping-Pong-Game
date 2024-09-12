import pygame
game = pygame.init()

screenSize = (800,600)

screen = pygame.display.set_mode((screenSize))
running = True

shootMusic = pygame.mixer.Sound('bullet.mp3')
shootMusic.set_volume(0.3)

rakcet1IMG = pygame.transform.scale(pygame.image.load('rakcet.png'),(10,80))
racket1X = 0
racket1Y = 260
racket1Change = 0
def rakcet1(x,y):
    screen.blit(rakcet1IMG,(x,y))

rakcet2IMG = pygame.transform.scale(pygame.image.load('rakcet.png'),(10,80))
racket2X = 790
racket2Y = 260
racket2Change = 0
def rakcet2(x,y):
    screen.blit(rakcet1IMG,(x,y))

ballIMG = pygame.transform.scale(pygame.image.load('ball.png'),(30,30))
ballX = 300
ballY = 200
ballXChange = 0.30
ballYChange = 0.30
def ball(x,y):
    screen.blit(ballIMG,(x,y))

while running:
    screen.fill((0,0,0))
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                racket1Change = -0.25
            if event.key==pygame.K_s:
                racket1Change = 0.25
            if event.key==pygame.K_UP:
                racket2Change = -0.25
            if event.key==pygame.K_DOWN:
                racket2Change = 0.25
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                racket1Change = 0
            if event.key==pygame.K_s:
                racket1Change = 0
            if event.key==pygame.K_UP:
                racket2Change = 0
            if event.key==pygame.K_DOWN:
                racket2Change = 0
    if racket1Y<=0:
        racket1Y = 0
    if racket1Y>=520:
        racket1Y = 520
    if racket2Y<=0:
        racket2Y = 0
    if racket2Y>=520:
        racket2Y = 520
    if ballY >= 570 or ballY <= 0:
        ballYChange *= -1
    if (racket1X <= ballX <= racket1X + 10) and (racket1Y <= ballY <= racket1Y + 80):
        shootMusic.play()
        ballXChange *= -1
    if (racket2X - 30 <= ballX <= racket2X) and (racket2Y <= ballY <= racket2Y + 80):
        shootMusic.play()
        ballXChange *= -1
    racket1Y += racket1Change
    racket2Y += racket2Change
    ballX += ballXChange
    ballY += ballYChange
    rakcet1(racket1X,racket1Y)
    rakcet2(racket2X,racket2Y)
    ball(ballX,ballY)
    pygame.display.update()

pygame.quit()