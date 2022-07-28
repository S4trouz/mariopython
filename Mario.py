import pygame
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

def mario():
    screen.blit(marioImg, (marioX,marioY))

#Goomba
goombaImg=pygame.image.load('goomba.png')
goombaImg=pygame.transform.scale(goombaImg,(70,70))
goombaX = 400
goombaY = 450

def goomba():
    screen.blit(goombaImg, (goombaX,goombaY))

#piece
coinImg=pygame.image.load('coin.png')
coinImg=pygame.transform.scale(coinImg,(70,70))
coinX = 100
coinY= 200

def coin():
    screen.blit(coinImg, (coinX,coinY))

#Lancer le jeu
running=True

while running:
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
                marioY_change = 1
            if event.key == pygame.K_DOWN:
                marioY_change = -1

    marioX += marioX_change
    marioY += marioY_change
    if marioX <=0:
        marioX = 0
    elif marioX >=750:
        marioX = 750
    if marioY <=0:
        marioY = 0
    elif marioY >=550:
        marioY = 550
    coin()
    mario()
    goomba()
    pygame.display.update()
