import pygame
from pygame import mixer
pygame.init()
pygame.time.Clock()

# SCREEN
BACKGROUND = 'Images/Background.JPG'
WIDTH = 1024
HEIGHT = 768
TITLE = "España Patria Querida"
GAME_ICON = 'Images/IconSpain.png'
FPS = 60
MUSIC = 'Sounds/GameMusic.wav'
FONT_NAME = 'freesansbold'

#PLAYER
PLAYER_IMAGE = 'Images/EspanaIcon.gif'
PLAYER_BULLET = 'Images/PlayerBullet.png'
PLAYER_ACC = 3
PLAYER_FRICTION = -0.2
PLAYER_GRAVITY = 0.8
PLAYER_JUMP_HEIGHT = -15
PLAYER_SHOT = "Sounds/PlayerShoot.wav"
PLAYER_JUMPS = "Sounds/PlayerJump.wav"


playerDeath = mixer.Sound('Sounds/PlayerDeath.wav')
enemy1Image = pygame.image.load ('Images/Enemy1.png')
enemyDeath = mixer.music.load('Sounds/EnemyDeath.wav')
enemyShoot = mixer.music.load('Sounds/EnemyShoot.wav')


# Variables de Platform (x , y, width, height)
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                (800, 600, 100, 20),
                (350, 450, 400, 20),
                (750, 250, 200, 20),
                (100, 150, 150, 20),
                (600, 50, 150, 20),]

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255, 0)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE


#ENEMY BULLET
enemyBulletImage = pygame.image.load ('Images/EnemyBullet.png')
enemyBulletX = 0
enemyBulletX_change = 0
enemyBulletY = 0
enemyBulletY_change = 0
enemyBullet_state = "ready"