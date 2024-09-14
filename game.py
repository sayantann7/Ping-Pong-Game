import pygame
game = pygame.init()

screenSize = (800,600)

# score1 = 0
# score2 = 0

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('assets/bg.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

pygame.display.set_caption("PING PONG")

pygame.display.set_icon(pygame.image.load('assets/icon.png'))

screen = pygame.display.set_mode((screenSize))
running = True
gameOver = False
winner = 1

shootMusic = pygame.mixer.Sound('assets/bullet.mp3')
shootMusic.set_volume(1.0)

rakcet1IMG = pygame.transform.scale(pygame.image.load('assets/rakcet.png'),(10,80))
racket1X = 0
racket1Y = 260
racket1Change = 0
def rakcet1(x,y):
    screen.blit(rakcet1IMG,(x,y))

rakcet2IMG = pygame.transform.scale(pygame.image.load('assets/rakcet.png'),(10,80))
racket2X = 790
racket2Y = 260
racket2Change = 0
def rakcet2(x,y):
    screen.blit(rakcet1IMG,(x,y))

ballIMG = pygame.transform.scale(pygame.image.load('assets/ball.png'),(30,30))
ballX = 300
ballY = 200
ballXChange = 0.30
ballYChange = 0.30
def ball(x,y):
    screen.blit(ballIMG,(x,y))

font = pygame.font.Font('assets/smallfont.ttf', 20)
bigfont = pygame.font.Font('assets/bigfont.ttf',60)


# def score_text(firstScore,secondScore):
#     p1score = font.render(f"PLAYER 1 SCORE : {score1}", True, (255,255,255))
#     p2score = font.render(f"PLAYER 2 SCORE : {score2}", True, (255,255,255))
#     screen.blit(p1score, (150, 0))
#     screen.blit(p2score, (550, 0))

def game_over():
    pygame.mixer.music.set_volume(0.0)
    game_over_text = bigfont.render("GAME OVER", True, (255,255,255))
    result_text = ""
    playAgainText = font.render("PRESS W TO PLAY AGAIN", True, (255,255,255))
    escText = font.render("PRESS ESC TO EXIT", True, (255,255,255))
    if winner==1:
        result_text = bigfont.render(f"PLAYER 1 WON!", True, (255,255,255))
    else:
        result_text = bigfont.render(f"PLAYER 2 WON!", True, (255,255,255))
    screen.blit(game_over_text,(290,200))
    screen.blit(result_text,(255,260))
    screen.blit(playAgainText,(325,330))
    screen.blit(escText,(340,350))

def welcome():
    welcome_text = bigfont.render("WELCOME TO", True, (255,255,255))
    title_text = bigfont.render("PING PONG!", True, (255,255,255))
    start_playing_text = font.render("PRESS W TO PLAY", True, (255,255,255))

    while True:
        screen.fill((0, 0, 0))
        screen.blit(welcome_text,(265,200))
        screen.blit(title_text,(280,260))
        screen.blit(start_playing_text,(327,330))
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  
                    return

welcome()

while running:
    screen.fill((0,0,0))
    pygame.mixer.music.set_volume(0.6)

    if gameOver:
        game_over()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    gameOver = False
                    ballX = 300
                    ballY = 200
                    ballXChange = 0.30
                    ballYChange = 0.30
                    racket1Y = 260
                    racket2Y = 260
                if event.key==pygame.K_ESCAPE:
                    running = False
        continue

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
    if ballX <= 0:
        gameOver = True
        winner = 2
    if ballX >= 770:
        gameOver = True
        winner = 1
    if (racket1X <= ballX <= racket1X + 10) and (racket1Y <= ballY <= racket1Y + 80):
        shootMusic.play()
        # score1 += 5
        ballXChange *= -1
    if (racket2X - 30 <= ballX <= racket2X) and (racket2Y <= ballY <= racket2Y + 80):
        shootMusic.play()
        # score2 += 5
        ballXChange *= -1
    racket1Y += racket1Change
    racket2Y += racket2Change
    ballX += ballXChange
    ballY += ballYChange
    rakcet1(racket1X,racket1Y)
    rakcet2(racket2X,racket2Y)
    ball(ballX,ballY)
    # score_text(score1,score2)
    pygame.display.update()

pygame.quit()