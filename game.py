import pygame
game = pygame.init()

screenSize = (800,600)

score1 = 0
score2 = 0

pygame.display.set_caption("PING PONG")

screen = pygame.display.set_mode((screenSize))
running = True
gameOver = False
winner = 1

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

font = pygame.font.Font('smallfont.ttf', 20)


def score_text(firstScore,secondScore):
    p1score = font.render(f"PLAYER 1 SCORE : {score1}", True, (255,255,255))
    p2score = font.render(f"PLAYER 2 SCORE : {score2}", True, (255,255,255))
    screen.blit(p1score, (150, 0))
    screen.blit(p2score, (550, 0))

clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()

while running:
    screen.fill((0,0,0))
    elapsed_time = int((pygame.time.get_ticks() - start_ticks) // 1000)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 600), 5)
    timer_text = font.render(f'TIME: {elapsed_time} s', True, (255,255,255))
    screen.blit(timer_text, (5, 575))
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
    if ballX <= 0:
        gameOver = True
        winner = 2
    if ballX >= 770:
        gameOver = True
        winner = 1
    if (racket1X <= ballX <= racket1X + 10) and (racket1Y <= ballY <= racket1Y + 80):
        shootMusic.play()
        score1 += 5
        ballXChange *= -1
    if (racket2X - 30 <= ballX <= racket2X) and (racket2Y <= ballY <= racket2Y + 80):
        shootMusic.play()
        score2 += 5
        ballXChange *= -1
    racket1Y += racket1Change
    racket2Y += racket2Change
    ballX += ballXChange
    ballY += ballYChange
    rakcet1(racket1X,racket1Y)
    rakcet2(racket2X,racket2Y)
    ball(ballX,ballY)
    score_text(score1,score2)
    pygame.display.update()

pygame.quit()