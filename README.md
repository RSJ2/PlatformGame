# PlatformGame
This is a plaform game for Final Project:

![](./Images/EspanaIcon.gif)

# CS50 FINAL PROJECT
## 2D game climbing the Covid-19 recovery

## Video Demo:  <URL HERE>

## Description:
#### This project is a fully working 2D game using python that takes user keyboard input to move a player icon to jump from platform to platform upwards, keeping track of score and reseting if a player dies/falls. My final project esentially tried many new concepts for me on 2D graphics making. I tried to make a very simple 2D platform game but using several functionalities not covered during the CS50 course. Firstly I moved away from the CS50 IDE onto Pycharm for coding in python. I analysed 3 different 2D graphics on python, Turtle, Pyglet and Pygame, and decided on the later due to the percieved more active support and advantages on 2D gaming. Despite game design nowadays being easier on platforms like Unity or LÖVE I was adiment to develop it on python. The course doesn't really touch on any game design so many of the concepts were new to me. First I sketched out what I wanted to do and how it would work on paper, a typical platform jumping game, with different icons, sounds, music and others. An important thing I focused on was the design, I wanted a small amout of code for an never ending game with minimal assets.

## The code:
#### The code is divided into three main files, one controls the game mechanics "Main2.py" the other two are "settings.py" and "sprites.py". One of the aims was to reduce the Main2.py file as much as posible and have an infinetly running game, assuming you are skilled enough!

#### The Main.py file has two main functions, "new()" and "run()" with "run()" having three other inner functions. But first, the Main2.py function initiates the game, by initating pygame, the game screen, the game icon and loading a music file. All of the variables in CAPITALS are defined in the settings.py file, which is left as a different file so that all the game settings can be reconfigured quickly and efficiently without chainging it in many places in the main code file, this is one of the features I feel leads to a good design:
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

#### There is then the "new" function, this esentially does two things, it loads the player class which is defined in the sprites.py file and it also loads the platforms, with the first platform being the only one that is different to all other platforms in the game as it represents the ground and covers the whole width of the screen. It then calls the "run()" function.
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


#### The "run()" function initself does nothing except to start a clock timer, and call the other 3 intrinsic functions which have the meat of the coding logic.
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

#### "events()" is the first function to get called and it just listens to user input to either move the player and call other funtions in the case a player jumps or shoots. The shooting functionality was developed since it was originally going to be a more arcade game and instead of being removed I decided to keep in the code in case anyone wants to reuse this in the future for their own improvements on top, but currently all it does is listen to the event and play a shooting sound to ensure the funtion works as a expected. The jump funtion is a bit more complicated but we'll get to it.
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

#### The code then calls the "update()" function which really makes the game tick. one of the best design features in my opinion is the way to generate platfomrms indefinetly as you move upwards. The way to achieve this was to create different platforms randomly withing a range infinetly and only have some other static assets like the player.
#### A new platform is added everytime there is less than 7 platforms on the screen. This is done through a loop with platforms of a random width range with the following lines:
	while len(self.platforms) < 7:
		width = random.randrange(100, 250)
		p = Platform(random.randrange(0, WIDTH - width), random.randrange(-75, -30), width, 20)
		self.platforms.add(p)
#### This function also controls the collision logic and is in charge of moving the platforms downwards and creating new ones once the player is reaching the top fourth of the screen.
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

#### It also controls the death event once a player hits the bottom of the screen.
            if self.player.rect.bottom > HEIGHT:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.vel.y, 10)
                    if sprite.rect.bottom < 0:
                        sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False

#### The last function that gets called is "draw()" which esentially draws the background and sprite positions on every refresh. The pygame-specific function ".split()" does just that refresh.
    def draw (self):
        self.background = pygame.image.load(BACKGROUND)
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        self.draw_text(str(self.score), 22, BLACK, WIDTH / 2, 15)
        pygame.display.flip()

#### There are other control functions such as "show_start_screen()" and "show_gameover_screen()" in charge of the running and ending the game functions.

#### The other code file "sprites.py" esentially holds the two main player control functions "update()" and "jump()". There is as previously mentioned another function for shooting which is only used to test future development functionality.

#### The file "settings.py" controls all of the external file inputs as well as things like the colour of platforms, the initial positions of platforms the game icons and others. These are all individualy configurable so anyone who wants to reuse this code has only to change the name of the files they are using for icons, bacgrounds, music, sunds and images.

## Neat features
#### The advantage of having a separate file with all the variables, means that the code doesn't have to be changed for any change to the game. Its extremely easy to change the player icon, sounds or even the platform colours.
#### The score updates everytime that the screen moves down once a player exceeds the top fourth of the screen and goes up by 10.
#### Another very cool feature is that I allowed players to disapear off one side of the screen to move to the other side, thus reaching platform that may look to be too far to jump from one side only. This is done with the following:
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH


## Future developments:
#### One of the things I ambitiously wanted to include was enemies on the platforms and a shooting capability for the player, however seeing as I evolved the game to a more addictive simple quick-game type, in the style of flappy bird or similar, it doesn't require that to be engaging and if anything it would complicate that too much.
#### I tried to make the game playable on a web browser. I spent many weeks hitting my head againts Skulp, this is a platform and seemingly the only way (I found) to embed python code on a website and be able to play from my Github Pages. However, running python code on html is one thing but installing libraries like pygame is another. The best way to run this online would be to recode the program on Love or Unity to then embed the code on html.
#### Another feature pending inclusion is the ability to give users capability of changing the colours of platforms or choose backgroud on the game screen, this can be done on the code really easily but potentially adding a dropdown could be an engaging feature for users.
#### Though not a future development, including enemies that shoot and being able to shoot back at them was one of the initial game design requirements I had, however, i felt it distracted from the main task of jumping up as far as one can go.
#### Lastly, in the same way that I would like platform colours to be configurable, I potentially could add different player icons and background pictures for users to configure their game as desired, with maybe even "in-app purchasable" ones to give the game a modern (yet anoying) game feel. These could be bought with points by including a running score tracker instead of a local variable that resets.
#### In order to do this I could look to build an SQL to store users and their points to keep track of their transactions much in the style of the CS50 Finance excercise.









