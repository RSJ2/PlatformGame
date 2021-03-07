import pygame
from pygame import mixer
from settings import *
pygame.init()
pygame.time.Clock()

# DEFINITIONS
def show_score (x,y):
    score = font.render("Score: "+str(scoreValue),True,(255,255,255))
    screen.blit(score, (x,y))

def game_over_text(x,y):
    gameover_text = gameover_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameover_text, (450, 350))

def player (x , y):
    screen.blit (playerImage, (x, y))

def enemy1 (x, y, i):
    screen.blit(enemy1Image, (x,y))

def playerBullet (x,y):
    global playerBullet_state
    playerBullet_state = "fire"
    screen.blit(playerBulletImage, (x + 16, y - 32))

#PLAYER BULLET COLLISION
def isCollision (enemy1X, enemy1Y, playerBulletX, playerBulletY):
    #distance = math.sqrt((math.pow(enemyX  - bulletX,2)+(math.pow(enemyY - bulletY,2))))
    #if distance < 27:
    #    return True
    #else:
    #    return False

    playerBulletX2 = playerBulletX + 32
    enemy1X2 = enemy1X + 64
    if playerBulletX2 >= enemy1X and playerBulletX <= enemy1X2 and playerBulletY == (enemy1Y + 64):
            return True
    else:
        return False
##### METER PARTE Y DE LA EQUACION (Y) PARA LA ALTURA



#GAME LOOP
running = True
while running:
    screen.blit(background,(0,0))  # Set screen back ground. For colour screen.fill((0 , 40, 0))
    for event in pygame.event.get():  # Listen to events from keyboard
        if event.type == pygame.QUIT:  # allow X in window to close program
            running = False

    if event.type == pygame.KEYDOWN:  # listen to ANY key being pressed down and check if left/right
        if event.key == pygame.K_LEFT:
            playerX_change = -0.5  # alter movement on the screen along x-axis
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.5
        if event.key == pygame.K_UP:
            playerY_change = -0.5
        if event.key == pygame.K_DOWN:
            playerY_change = 0.5
        if event.key == pygame.K_SPACE:  # when space is hit release bullet, fix the x position and change y position
            if playerBullet_state is "ready":
                playerShoot.set_volume(0.3)
                playerShoot.play (0,500,0)
                playerBulletX = playerX
                playerBulletY = playerY
                playerBullet (playerBulletX, playerBulletY)
    if event.type == pygame.KEYUP:  # check for key release and stop moving
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: # or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            playerX_change = 0
            playerY_change = 0

    # PLAYER MOVEMENT
    playerX += playerX_change  # assign new value to X axis
    if playerX > 768:  # screen boundaries
        playerX = 768
    if playerX < 0:
        playerX = 0
    playerY += playerY_change  # assign new value to Y axis
    if playerY > 768:  # screen boundaries
        playerY = 768
    if playerY < 0:
        playerY = 0





    player(playerX, playerY)
    pygame.display.update()