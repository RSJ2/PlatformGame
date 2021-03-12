# PlatformGame
This is a plaform game for Final Project:



Desempeño - TTCC N05 - N08


# CS50 FINAL PROJECT
## 2D game climbing the Covid-19 recovery

### Video Demo:  <URL HERE>

### Description:
#### This project is a fully working 2D game using python that takes user keyboard input to move a player icon to jump from platform to platform upwards, keeping track of score and reseting if a player dies/falls.
#### My final project esentially tried many new concepts for me on 2D graphics making.
#### I tried to make a very simple 2D platform game but using several functionalities not covered during the CS50 course.
#### Firstly I moved away from the CS50 IDE onto Pycharm for coding in python.
#### I analysed 3 different 2D graphics on python, Turtle, Pyglet and Pygame, and decided on the later due to the percieved more active support and advantages on 2D gaming.
#### Despite game design nowadays being easier on platforms like Unity or LÖVE I was adiment to develop it on python.
#### The course doesn't really touch on any game design so many of the concepts were new to me
#### First I sketched out what I wanted to do and how it would work on paper, a typical platform jumping game, with different icons, sounds, music and others.
#### An important thing I focused on was the design, I wanted a small amout of code for an never ending game with minimal assets.

### The code:
#### The code is divided into three main files, one controls the game mechanics "Main2.py" the other two are "settings.py" f
#### The way to achieve this was to create different platforms randomly withing a range infinetly and only have some other static assets like the player.
#### A new platform is added everytime there is less than 7 platforms on the screen. This is done through a loop with platforms of a random width range with the following lines:
	while len(self.platforms) < 7:
		width = random.randrange(100, 250)
		p = Platform(random.randrange(0, WIDTH - width), random.randrange(-75, -30), width, 20)
		self.platforms.add(p)
#### The program takes continuous input from the user such as the arrow keys or the spacebar  


### Neat features
#### The advantage of having a separate file with all the variables, means that the code doesn't have to be changed for any change to the game. Its extremely easy to change the player icon, sounds or even the platform colours.
#### The score updates everytime that the screen 


### Future developments:
#### One of the things I ambitiously wanted to include was enemies on the platforms and a shooting capability for the player.
#### I spent many weeks hitting my head againts Skulp, this is a platform and seemingly the only way (I found) to embed python code on a website and be able to play from my Github Pages.
#### Another feature pending inclusion is the ability to give users capability of changing the colours of platforms or choose backgroud.









