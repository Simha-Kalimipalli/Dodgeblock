# Unit  2-Assignment 2-Q5
# By: Simha Kalimipalli

"""
Started Apr 17, 2019

Modified: main program started  Apr 17, 2019
                    program edited Apr 18, 2019
                    program edited Apr 19, 2019
                     program finished Apr 21 2019
                   added comments/final edits on Apr 22, 2019

                   December 2020: remastered game  - added sound, timing, better graphics

Question "Wow Mr. Harris using Pygame"

The base of the program was inspired by car.py given in class
However, Minimal/No Code was directly borrowed for this question

All images were created by me

"""

# import the necessary libraries (pygame, random)
import pygame, random, sys,time

# initiallize pygame
pygame.init()

# load coin image
coin_sprite = pygame.image.load("images/Coin_image.png")

# load audio
hit_sound = pygame.mixer.Sound("audio/hitting_sound.mp3")
coin_sound = pygame.mixer.Sound("audio/coin_sound.wav")
victory_sound = pygame.mixer.Sound("audio/victory_sound.wav")
# *****************************************************************************

# Creates chicken class (for player object)
class Chicken(pygame.sprite.Sprite):
    # This class represents a car. It derives from the "Sprite" class in Pygame.

    # initializes class
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # initializes color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the "chicken" - a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # gets the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    # Function for player moving right
    def moveRight(self, pixels):
        self.rect.x += pixels

    # Function for player moving left
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    # Function for player moving Up
    def moveUp(self, pixels):
        self.rect.y -= pixels

    # Function for player moving Down

    def moveDown(self, pixels):
        self.rect.y += pixels

#  Car Class (for rectangles that appear on screen)
class Car(pygame.sprite.Sprite): #derives from sprite class

    # initializes class
    def __init__(self, color, width, height,speed):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # initializes the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the "car" - a rectangle
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.dx = 5
        self.dy = 0

        # Instead we could load a proper pciture of a car...
        # self.image = pygame.image.load("car.png").convert_alpha()

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.speed = speed
        self.width = width
        self.height = height
        self.color = color

    # Function for "car" moving forward
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    # Function for "car" moving backward
    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    # Function for "car" changing speed
    def changeSpeed(self, speed):
        self.speed = speed

    # Function for "car" changes colour
    def repaint(self, color):
        self.color = color
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

# creates class for the coin objects
class Coin(pygame.sprite.Sprite): # derives from sprite class

    # initiallizes class
    def __init__(self, color, radius,speed):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = coin_sprite
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.centery = 50
        self.dx = 10
        self.dy = 0


        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        self.speed = speed
        self.radius = radius
        self.color = color


# *****************************************************************************

# *************** F U N C T I O N S BEGIN ************************************
# function for displaying text on the screen
def display_text(message, setx_m, sety_m):
    my_text = message
    our_font = pygame.font.SysFont("Calibri", 26)
    # render the text now
    produce_text = our_font.render(my_text, 1, BLACK)
    screen.blit(produce_text, (setx_m, sety_m))

# *************** F U N C T I O N S END *************************************

# *************** M A I N - P R O G R A M BEGIN ************************************
# initializing pygame
pygame.init()

# Defining colours
GREEN = (50, 205, 50)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLUE = (0,0,255)
GOLD = (212,175,55)
ORANGE = (255,165,0)
BLACK = (0,0,0)
colour_List = (RED,PURPLE,BLUE,ORANGE)

#  Open a new window/initiallizing screen
SCREENWIDTH = 990
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

# Creates caption for window
pygame.display.set_caption("Dodgeblock")

# Initialize Sprites and add them to the Sprite List group
# List of Sprites that will be used in the game
all_sprites_list = pygame.sprite.Group()
blocks_hit_list= pygame.sprite.Group()
car_sprites_list = pygame.sprite.Group()
coin_sprite_list = pygame.sprite.Group()
coin_hit_list = pygame.sprite.Group()

# creates Player 1 sprite and adds it to all sprites list
chick_striker = Chicken(BLACK, 20, 30)
chick_striker.rect.x = 10
chick_striker.rect.y = 200
all_sprites_list.add(chick_striker)

# creates Car 1 sprite and adds it to all sprites list and car sprites list
Car_1 = Car(BLUE,50,50,random.randint(50, 100))
Car_1.rect.x = 60
Car_1.rect.y = 0
all_sprites_list.add(Car_1)
car_sprites_list.add(Car_1)

# creates car 2 sprite and adds it to all sprites list and car sprites list
Car_2 = Car(PURPLE,50,50,random.randint(50, 100))
Car_2.rect.x = 160
Car_2.rect.y = 20
all_sprites_list.add(Car_2)
car_sprites_list.add(Car_2)

# creates car 3 sprite and adds it to all sprites list and car sprites list
Car_3 = Car(RED,50,50,random.randint(50, 100))
Car_3.rect.x =260
Car_3.rect.y = -20
all_sprites_list.add(Car_3)
car_sprites_list.add(Car_3)

# creates car 4 sprite and adds it to all sprites list and car sprites list
Car_4 = Car(RED,50,100,random.randint(50, 100))
Car_4.rect.x =60
Car_4.rect.y = 200
all_sprites_list.add(Car_4)
car_sprites_list.add(Car_4)

# creates Car 5 sprite and adds it to all sprites list and car sprites list
Car_5 = Car(PURPLE,50,50,random.randint(50, 100))
Car_5.rect.x = 160
Car_5.rect.y = 200
all_sprites_list.add(Car_5)
car_sprites_list.add(Car_5)

# creates car 6 sprite and adds it to all sprites list and car sprites list
Car_6 = Car(RED,50,50,random.randint(50, 100))
Car_6.rect.x =260
Car_6.rect.y = 200
all_sprites_list.add(Car_6)
car_sprites_list.add(Car_6)

# creates car 7 sprite and adds it to all sprites list and car sprites list
Car_7 = Car(RED,50,200,random.randint(50, 100))
Car_7.rect.x =260
Car_7.rect.y = 200
all_sprites_list.add(Car_7)
car_sprites_list.add(Car_7)

# creates car 8 sprite and adds it to all sprites list and car sprites list
Car_8 = Car(RED,50,200,random.randint(50, 100))
Car_8.rect.x =360
Car_8.rect.y = 0
all_sprites_list.add(Car_8)
car_sprites_list.add(Car_8)

# creates car 9 sprite and adds it to all sprites list and car sprites list
Car_9 = Car(RED,50,40,random.randint(50, 100))
Car_9.rect.x =490
Car_9.rect.y = 0
all_sprites_list.add(Car_9)
car_sprites_list.add(Car_9)

# creates car 10 sprite and adds it to all sprites list and car sprites list
Car_10 = Car(RED,50,300,random.randint(50, 100))
Car_10.rect.x =490
Car_10.rect.y = 0
all_sprites_list.add(Car_10)
car_sprites_list.add(Car_10)

# creates car 11 sprite and adds it to all sprites list and car sprites list
Car_11 = Car(RED,50,50,random.randint(50, 100))
Car_11.rect.x =590
Car_11.rect.y = 0
all_sprites_list.add(Car_11)
car_sprites_list.add(Car_11)

# creates car 12 sprite and adds it to all sprites list and car sprites list
Car_12 = Car(RED,50,50,random.randint(50, 100))
Car_12.rect.x =590
Car_12.rect.y = 0
all_sprites_list.add(Car_12)
car_sprites_list.add(Car_12)

# creates car 13 sprite and adds it to all sprites list and car sprites list
Car_13 = Car(RED,50,50,random.randint(50, 100))
Car_13.rect.x =690
Car_13.rect.y = 0
all_sprites_list.add(Car_13)
car_sprites_list.add(Car_13)

# creates All coins sprites and adds it to all sprites list and coin sprites list
for i in range(25):
    tmpx = random.randrange(40, 740)
    tmpy = random.randrange(0, 550)
    tmpbox = Coin(GOLD, 50, 1)
    tmpbox.rect.x = tmpx
    tmpbox.rect.y = tmpy
    all_sprites_list.add(tmpbox)
    coin_sprite_list.add(tmpbox)

##########################################3

# while loop of game
carryOn = True

# defining pygame clock
clock = pygame.time.Clock()

# Initializing variables that will be used in the while loop
coins_collect = 0
hit_counter = 0
end_game = 0
end_time = 0
sound_count = 0

# M A I N  L O O P ######################################################
while carryOn:
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            carryOn = False

    # allows the player to move the player object (chick_striker) in all directions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        chick_striker.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        chick_striker.moveRight(5)
    if keys[pygame.K_UP]:
        chick_striker.moveUp(5)
    if keys[pygame.K_DOWN]:
        chick_striker.moveDown(5)

        # Game Logic - repaints cars when the return on screen
    for car in car_sprites_list:
        car.moveForward(1)
        if car.rect.y > SCREENHEIGHT:
            car.repaint(random.choice(colour_List))
            car.rect.y = -200

    # updates car sprite list
    car_sprites_list.update()

    # checks for collision between player and cars
    blocks_hit_list = pygame.sprite.spritecollide(chick_striker,car_sprites_list,False)

    # counts hits
    score_it =0
    for block in blocks_hit_list:
        score_it = score_it + 1

    if score_it > 0:
        # Places the player back to starting position if hit
        chick_striker.rect.x = 10
        chick_striker.rect.y = 200
        hit_counter= hit_counter+1
        hit_sound.play()

    # checks for collision between player and coins
    coin_hit_list = pygame.sprite.spritecollide(chick_striker, coin_sprite_list, True)

    # Adds to the number of coins collected
    for coin in coin_hit_list:
        coins_collect = coins_collect + 1
        coin_sound.play()

    # Game Logic
    all_sprites_list.draw(screen)

    # changes Screen colour
    screen.fill(GREEN)

    # Draw The Road
    pygame.draw.rect(screen, GREY, [40, 0, 400, SCREENHEIGHT])
    pygame.draw.rect(screen, GREY, [480, 0, 290, SCREENHEIGHT])

    # Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140, 0], [140, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [240, 0], [240, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [340, 0], [340, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [560, 0], [560, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [660, 0], [660, SCREENHEIGHT], 5)
    pygame.draw.line(screen, WHITE, [760, 0], [760, SCREENHEIGHT], 5)

    # Draws Message Box
    pygame.draw.rect(screen, GOLD, [775,0, 300,220])
    pygame.draw.rect(screen, GOLD, [775,240, 300,200])

    #display time in seconds
    if ( end_game == 0):
        time1 = pygame.time.get_ticks()
    else:
        time1 = end_time

    time_sec = time1 / 1000
    display_text("Time: "+str(time_sec) +"s", 780, 390)

    # Display whether player has lost, won or "keep Trying" if neither has been accomplished
    if coins_collect == 25 and hit_counter <=10 and time_sec < 60:
        pygame.draw.rect(screen, BLACK, [775, 241, 300, 44], 7)
        pygame.draw.rect(screen, (0, 250, 40), [775, 241, 300, 44])
        display_text("You Win!", 780, 250)

        # time of the end of game
        end_game = 1
        end_time = time1

        # plays victory sound
        if sound_count == 0:
            victory_sound.play()
            sound_count = 1

    elif coins_collect < 25 and hit_counter < 10 and (time_sec < 60):
        pygame.draw.rect(screen, BLACK, [775, 239, 300, 44],2)
        display_text("Keep Trying! ", 780, 250)

    elif (coins_collect >0 and hit_counter >= 10 and end_game==0) or (time_sec>60):
        pygame.draw.rect(screen, BLACK, [775, 241, 300, 44], 7)
        pygame.draw.rect(screen, (250, 0, 40), [775, 241, 300, 44])
        display_text("You Lose", 780, 250)

       # displays counter for  number of  boxes hit
    display_text("You hit " + str(hit_counter) + " boxes", 780, 290)

    # Draws all of the sprites
    all_sprites_list.draw(screen)

    # displays counter for the number of coins collected
    display_text("Coins Collected: " + str(coins_collect), 780, 340)
    x = 30

    # displays instructions for the game
    display_text("Instructions:", 780, x-25)
    display_text("1. Use arrow keys ",780,x)
    display_text("to control your", 780, x+20)
    display_text("player (black box)",780,x+40)
    display_text("2. Don't get hit", 780, x+80)
    display_text("by the rectangles!", 780, x+100)
    display_text("3. Collect the ", 780, x+140)
    display_text("coins in 60s", 780, x+160)

    # Refresh Screen
    pygame.display.flip()

    # Number of frames per secong e.g. 60
    clock.tick(60)

# Quits pyagme
pygame.quit()

# *************** M A I N - P R O G R A M END ************************************

