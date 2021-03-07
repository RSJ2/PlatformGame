import pygame
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(GAME_ICON))
        self.clock = pygame.time.Clock()
        self.music = mixer.music.load(MUSIC)
        self.music = mixer.music.set_volume(0.1)
        self.music = mixer.music.play(-1)
        self.running = True
        self.font_name = pygame.font.match_font(FONT_NAME)


    def new (self):
        self.score = 0
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for items in PLATFORM_LIST:
            p = Platform(*items)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        self.all_sprites.update()
        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0

        # if player reaches top 1/4 of screen
            if self.player.rect.top <= HEIGHT / 3:
                self.player.pos.y += abs(self.player.vel.y + 15)
                for items in self.platforms:
                    items.rect.y += abs(self.player.vel.y + 15)
                    if items.rect.top >= HEIGHT:
                        items.kill()
                        self.score += 10

            # spawn new platforms to keep same average number
            while len(self.platforms) < 7:
                width = random.randrange(100, 250)
                p = Platform(random.randrange(0, WIDTH - width),
                            random.randrange(-75, -30),
                            width, 20)
                self.platforms.add(p)
                self.all_sprites.add(p)

            # Dying
            if self.player.rect.bottom > HEIGHT:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.vel.y, 10)
                    if sprite.rect.bottom < 0:
                        sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()




    def draw (self):
        self.background = pygame.image.load(BACKGROUND)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, BLACK, WIDTH / 2, 15)
        pygame.display.flip()


    def show_start_screen (self):
        pass
    def show_gameover_screen (self):
        pass

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_gameover_screen()


pygame.quit()

