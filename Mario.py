import pygame
import random
pygame.init()

#Générer la fenêtre du jeu 
pygame.display.set_caption("Mario")
#Background et icon 
icon=pygame.image.load('mario.png')
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((800,600))
color = (58, 157, 35)
screen.fill(color)
pygame.display.flip()

#Mario
marioImg=pygame.image.load('mario.png')
marioImg=pygame.transform.scale(marioImg,(70,70))
marioX = 270
marioY = 380
marioX_change=0
marioY_change=0

def mario():
    screen.blit(marioImg, (marioX,marioY))

#Goomba
goombaImg=pygame.image.load('goomba.png')
goombaImg=pygame.transform.scale(goombaImg,(70,70))
goombaX = random.randint(0, 730)
goombaY = random.randint(0, 530)

def goomba():
    screen.blit(goombaImg, (goombaX,goombaY))

#piece
coinImg=pygame.image.load('coin.png')
coinImg=pygame.transform.scale(coinImg,(70,70))
coinX = random.randint(0,730)
coinY= random.randint(0,530)

def coin():
    screen.blit(coinImg, (coinX,coinY))

score=0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

#Lancer le jeu
running=True

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False  

    
    #controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                marioX_change = -1 
            if event.key == pygame.K_RIGHT:
                marioX_change = 1
            if event.key == pygame.K_UP:
                marioY_change = -1
            if event.key == pygame.K_DOWN:
                marioY_change = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                marioX_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                marioY_change = 0


    marioX += marioX_change
    marioY += marioY_change

    if marioX <=0:
        marioX = 0
    elif marioX >=730:
        marioX = 730
    if marioY <=0:
        marioY = 0
    elif marioY >=530:
        marioY = 530
    
    #Collision avec la pièce
    if marioX < coinX + 70 and marioX + 70 > coinX and marioY < coinY + 70 and marioY + 70 > coinY:
        coinX = random.randint(0,730)
        coinY = random.randint(0,530)
        score += 1

        goombaX = random.randint(0,730)
        goombaY = random.randint(0,530)
    
    coin()
    mario()
    goomba()
    show_score()
    pygame.display.update()
