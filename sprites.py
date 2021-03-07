from settings import *
import pygame
import pygame.mixer
import pygame.math
import pygame.time
vec = pygame.math.Vector2

class Player (pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(PLAYER_IMAGE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, 600)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = PLAYER_JUMP_HEIGHT
            PLAYER_JUMP = mixer.Sound(PLAYER_JUMPS)
            mixer.Sound.set_volume(PLAYER_JUMP, 0.2)
            mixer.Sound.play(PLAYER_JUMP)

    def shoot (self):
        self.ready_fire = True
        PLAYER_SHOOT = mixer.Sound(PLAYER_SHOT)
        mixer.Sound.set_volume(PLAYER_SHOOT, 0.4)
        if self.ready_fire:
            mixer.Sound.play(PLAYER_SHOOT)

            #self.bullet_image = pygame.image.load(PLAYER_BULLET)
            #self.rect = self.bullet_image.get_rect()

            self.ready_fire = False
            pygame.time.delay(200)
        self.ready_fire = True


    def update(self):
        pygame.mixer.init()
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys [pygame.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys [pygame.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        self.acc.x += self.vel.x * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos



class Platform (pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y