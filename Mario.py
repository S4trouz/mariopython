import pygame
import random
import math
#initialisation de pygame
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

#Chargement et redimension de Mario
marioImg=pygame.image.load('mario.png')
marioImg=pygame.transform.scale(marioImg,(70,70))
marioX = 270
marioY = 380
marioX_change=0
marioY_change=0

#Fonction pour afficher Mario
#Fonction pour afficher Mario
def mario():
    screen.blit(marioImg, (marioX,marioY))

#Chargement et redimension du Goomba
#Chargement et redimension du Goomba
goombaImg=pygame.image.load('goomba.png')
goombaImg=pygame.transform.scale(goombaImg,(70,70))

#Affichage du Goomba à une position aléatoire
def generate_random_goomba_position():
    global goombaX, goombaY
    while True:
        goombaX=random.randint(0, 730)
        goombaY=random.randint(0,530)

#Déplacement du goomba
goomba_speed = 0.2
goomba_direction = 'horizontal'  # Alternance de 'horizontal' et 'vertical'
goombaX_change = goomba_speed
goombaY_change = 0

#Affichage du Goomba à une position aléatoire
def generate_random_goomba_position():
    global goombaX, goombaY
    while True:
        goombaX=random.randint(0, 730)
        goombaY=random.randint(0,530)
        if math.sqrt((goombaX - marioX) ** 2 + (goombaY - marioY) ** 2) > 150:
            break
generate_random_goomba_position()

#Fonction pour afficher le Goomba sur l'écran 
        if goombaX != marioX and goombaY != marioY:
            break
generate_random_goomba_position()

#Fonction pour afficher le Goomba sur l'écran 
def goomba():
    screen.blit(goombaImg, (goombaX,goombaY))

#Chargement et redimension de la pièce
#Chargement et redimension de la pièce
coinImg=pygame.image.load('coin.png')
coinImg=pygame.transform.scale(coinImg,(70,70))

#Affichage à une position aléatoire de la pièce
def generate_random_coin_position():
    global coinX, coinY
    while True:
        coinX=random.randint(0, 730)
        coinY=random.randint(0, 530)

#Affichage à une position aléatoire de la pièce
def generate_random_coin_position():
    global coinX, coinY
    while True:
        coinX=random.randint(0, 730)
        coinY=random.randint(0, 530)

        if coinX != marioX and coinY != marioY and coinX != goombaX and coinY != goombaY:
            break
generate_random_coin_position()

#Fonction pour afficher la pièce
        if (math.sqrt((coinX - marioX) ** 2 + (coinY - marioY) ** 2) > 150 and
                math.sqrt((coinX - goombaX) ** 2 + (coinY - goombaY) ** 2) > 150):
            break
generate_random_coin_position()

#Fonction pour afficher la pièce
def coin():
    screen.blit(coinImg, (coinX,coinY))

#Score initial
score=0

#Police d'affichage du score
font = pygame.font.Font(None, 36)

#Fonction pour afficher le score sur l'écran
def show_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

#Chargement et redimension des icônes de vie
#Chargement et redimension des icônes de vie
life_icon = pygame.image.load('life_icon.png')
life_icon = pygame.transform.scale(life_icon, (40, 40))

#Nombre de vie initial

#Nombre de vie initial
num_lives = 3

#Fonction pour afficher les vies
#Fonction pour afficher les vies
def show_lives():
    for i in range(num_lives):
        screen.blit(life_icon, (750 - (i * 40), 10))

#Police d'affichage du gameover
#Police d'affichage du gameover
game_over_font = pygame.font.Font(None, 100)

#Fonction pour afficher le gameover
#Fonction pour afficher le gameover
def show_game_over():
    game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))
    text_rect = game_over_text.get_rect(center=(400, 300))
    screen.blit(game_over_text, text_rect)


#Lancer le jeu
running=True
game_over=False


# Timer pour alterner les direction automatiques
change_direction_time = 3000  # en millisecondes
last_direction_change_time = pygame.time.get_ticks()

while running:
    screen.fill(color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False  

    if not game_over:
    #Contrôles
    #Contrôles
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

    #Mouvement de Mario
    #Mouvement de Mario
    marioX += marioX_change
    marioY += marioY_change
    #Limites de l'écran
    #Limites de l'écran
    if marioX <=0:
        marioX = 0
    elif marioX >=730:
        marioX = 730
    if marioY <=0:
        marioY = 0
    elif marioY >=530:
        marioY = 530
    
    #Collision avec le Goomba

    #Mouvement du goomba quand le score atteint 10
    if score >= 10:
        current_time = pygame.time.get_ticks()
        if current_time - last_direction_change_time > change_direction_time:
            # Alterner la direction du Goomba
            if goomba_direction == 'horizontal':
                goomba_direction = 'vertical'
                goombaX_change = 0
                goombaY_change = goomba_speed * random.choice([-1, 1])
            else:
                goomba_direction = 'horizontal'
                goombaX_change = goomba_speed * random.choice([-1, 1])
                goombaY_change = 0
            last_direction_change_time = current_time

        goombaX += goombaX_change
        goombaY += goombaY_change
        
        #Change de direction si le goomba atteint les bords de l'écran
        if goombaX <= 0 or goombaX >=730:
            goombaX_change *= -1
        if goombaY <= 0 or goombaY >=530:
            goombaY_change *= -1

    #Collision avec le Goomba
    if marioX < goombaX + 70 and marioX + 70 > goombaX and marioY < goombaY + 70 and marioY + 70 > goombaY:
        goombaX = random.randint(0, 730)
        goombaY = random.randint(0, 530)
        num_lives -= 1

        if num_lives == 0:
            game_over = True

            generate_random_goomba_position()
            num_lives -= 1
            if num_lives == 0:
                game_over = True

    #Collision avec la pièce
    if marioX < coinX + 70 and marioX + 70 > coinX and marioY < coinY + 70 and marioY + 70 > coinY:
            generate_random_coin_position()
            score += 1
            # Augmenter la vitesse du gomba chaque fois que le score est un multiple de 10
            if score % 10 ==0:
                goomba_speed += 0.1
            generate_random_goomba_position()
            
    
    #Affichage des élément du jeu
    #Affichage des élément du jeu
    coin()
    mario()
    goomba()
    show_score()
    show_lives()

    #Affichage du gameover
    #Affichage du gameover
    if game_over:
        screen.fill((0, 0, 0))
        show_game_over()
    pygame.display.update()
