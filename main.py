import pygame
# import time

screenHeight = 400
screenWidth = 700
#THE FOLLOWING IMAGES STILL NEED TO BE UPLOADED HERE: haunted.jpg, leaderboardButton.jpg, exitButton.jpg, optionsButton.jpg, startButton.jpg, and any other newer files. File Management was done by me (Ben) to be as straightforward as possible. :)

#loading images and game sizing
screen = pygame.display.set_mode((screenWidth, screenHeight))
menuScreen = pygame.image.load("menuFullScreen.png").convert()

bookshelfOne = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf1.jpeg").convert()
bookshelfTwo = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf2.jpg").convert()
bookshelfThree = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf3.jpg").convert()
bookshelfFour = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf4.jpeg").convert()
bookshelfFive = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf5.jpeg").convert()
bookshelfSix = pygame.image.load(
    "assets/images/Library/bookshelves/bookshelf6.jpeg").convert()

leftArrowImage = pygame.image.load(
    "assets/buttons/all-screens/leftArrow.jpg").convert()
rightArrow = pygame.image.load(
    "assets/buttons/all-screens/rightArrow.jpg").convert()

##########################################################################################
# Created a variable which holds an image of the dialog button
dialogButtonImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialogButton.jpeg")
# Created a variable which holds an image of the dialog
dialogImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialog.jpeg")
##########################################################################################

leverOn = pygame.image.load(
    "assets/images/Library/puzzle-1/lever/leverOn.png").convert()
leverOff = pygame.image.load(
    "assets/images/Library/puzzle-1/lever/leverOff.png").convert()

oneOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/1clock.png").convert()
twoOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/2clock.png").convert()

#we have duplicates of three and four o'clock because of the wall needing two still clocks

threeOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/3clock.png").convert()
threeOClock2 = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/3clock2.png").convert()

fourOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/4clock.png").convert()
fourOClock2 = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/4clock2.png").convert()

fiveOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/5clock.png").convert()
sixOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/6clock.png").convert()
sevenOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/7clock.png").convert()
eightOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/8clock.png").convert()
nineOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/9clock.png").convert()
tenOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/10clock.png").convert()
elevenOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/11clock.png").convert()
twelveOClock = pygame.image.load(
    "assets/images/Library/puzzle-1/clocks/12clock.png").convert()

inventoryImage = pygame.image.load(
    "assets/images/inv/inventoryIcon.png").convert_alpha()
inventoryHotbar = pygame.image.load(
    "assets/images/inv/inventoryHotbar.png").convert_alpha()
inventoryTextThing = pygame.image.load(
    "assets/images/inv/inventoryTextThing.png").convert_alpha()
keyImage = pygame.image.load("assets/images/inv/keyImage.png").convert_alpha()
inventoryBackground = pygame.image.load(
    "assets/images/inv/inventoryBackground.jpeg").convert_alpha()


#classes for defining image, scale, and location
class imageScaling():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


#class for defining if image clicked (not useful when dealing with specific screens)


class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action


menuScreen = imageScaling(0, 0, menuScreen, 0.5)

bookshelfOne = imageScaling(0, 0, bookshelfOne, 3)
bookshelfTwo = imageScaling(0, 0, bookshelfTwo, 3)
bookshelfThree = imageScaling(0, 0, bookshelfThree, 1)
bookshelfFour = imageScaling(0, 0, bookshelfFour, 3)
bookshelfFive = imageScaling(0, 0, bookshelfFive, 3)
bookshelfSix = imageScaling(0, 0, bookshelfSix, 3)

leftArrowButton = Button(100, screenHeight / 2, leftArrowImage, 0.3)
rightArrow = Button(540, screenHeight / 2, rightArrow, 0.3)

##########################################################################################
# Created a button (techincally just an image object) which includes a way to scale the image using a class named "imageScale" and this object also includes a way to draw it with the method within Button class named "draw()"
dialogButtonImageObject = Button(1, 1, dialogButtonImageObject, 0.05)
dialogImageObject = Button(100, screenHeight / 8, dialogImageObject, 1.6)
##########################################################################################

leverOn = imageScaling(310, 175, leverOn, 0.03)
leverOff = imageScaling(310, 175, leverOff, 0.03)
keyImageButton = Button(440, 180, keyImage, 0.3)
inventoryKey = Button(197, 297, keyImage, 0.1)

inventoryIcon = imageScaling(600, 10, inventoryImage, 0.3)
inventoryIcon2 = imageScaling(100, 300, inventoryImage, 0.4)
inventoryHotbar = imageScaling(200, 300, inventoryHotbar, 0.5)
inventoryTextThing = imageScaling(180, 40, inventoryTextThing, 0.5)
inventoryBackground = imageScaling(0, 0, inventoryBackground, 3)

#adding clock times individually to test
oneOClock = imageScaling(390, 40, oneOClock, 0.5)
twoOClock = imageScaling(390, 40, twoOClock, 0.5)
threeOClock = imageScaling(390, 40, threeOClock, 0.5)
fourOClock = imageScaling(390, 40, fourOClock, 0.5)
fiveOClock = imageScaling(390, 40, fiveOClock, 0.5)
sixOClock = imageScaling(390, 40, sixOClock, 0.5)
sevenOClock = imageScaling(390, 40, sevenOClock, 0.5)
eightOClock = imageScaling(390, 40, eightOClock, 0.5)
nineOClock = imageScaling(390, 40, nineOClock, 0.5)
tenOClock = imageScaling(390, 40, tenOClock, 0.5)
elevenOClock = imageScaling(390, 40, elevenOClock, 0.5)
twelveOClock = imageScaling(390, 40, twelveOClock, 0.5)

threeOClock2 = imageScaling(160, 40, threeOClock2, 0.5)
fourOClock2 = imageScaling(275, 40, fourOClock2, 0.5)

imageList = [
    bookshelfOne, bookshelfTwo, bookshelfThree, bookshelfFour, bookshelfFive,
    bookshelfSix
]
clockTimes = [
    oneOClock, twoOClock, threeOClock, fourOClock, fiveOClock, sixOClock,
    sevenOClock, eightOClock, nineOClock, tenOClock, elevenOClock, twelveOClock
]
inventory = []
inventoryOpen = False

clockIndex = 11  #clock time (it starts at 12:00)
imageIndex = 0  #rotates images of library
leverState = False  #false until lever clicked
keySelected = False  #false until key in inventory is clicked

run = True
imageOne = False  #used to cycle images and put arrows
clocksIteration = True  #avoid stacked images and lag
menuOpen = True

while run:
    while menuOpen == True:
        menuScreen.draw()
        menuOpen = False
        # pygame method named "Rect" takes in parameters (left, top, width, height)
        startButtonRect = pygame.Rect(455, 100, 135, 50)
        optionButtonRect = pygame.Rect(455, 180, 130, 50)
        rankingButtonRect = pygame.Rect(455, 260, 130, 50)
        exitButtonRect = pygame.Rect(455, 340, 130, 50)

        ##########################################################################################
        # Context: Within this "while loop" it checks using a variable named "menuOpen" if it is the first enternace and draws the menu using the "Button.class" "draw()" method. Since this is the first while loop which draws the very first image we will place our dialog button image object here as well when we enter using the "draw()" method of the variable we created
        dialogButtonImageObject.draw()
        ##########################################################################################

    while imageOne == True:
        imageList[imageIndex].draw()
        leftArrowButton.draw()
        rightArrow.draw()
        imageOne = False

    if imageIndex == 1 and clocksIteration == True:
        threeOClock2.draw()
        fourOClock2.draw()
        clockTimes[clockIndex].draw()
        clocksIteration = False
        leverOff.draw()

    #for all rooms
    if leftArrowButton.draw():
        print('Left arrow clicked')
        if imageIndex == 0:
            imageIndex = len(imageList) - 1
        if imageIndex == 2:
            clocksIteration = True
            imageIndex -= 1
        else:
            imageIndex -= 1
        screen.fill((0, 0, 0, 0))
        imageList[imageIndex].draw()
        print(imageIndex)

    if rightArrow.draw():
        print('Right arrow clicked')
        if imageIndex == len(imageList) - 1:
            imageIndex = 0
        if imageIndex == 0:
            clocksIteration = True
            imageIndex += 1
        else:
            imageIndex += 1
        screen.fill((0, 0, 0, 0))
        imageList[imageIndex].draw()
        print(imageIndex)
    pygame.display.update()

    for event in pygame.event.get():
        #pygame.quit() will run and close window
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            #This is to allow pressing the 'e' key to open the inv and then close it
            if inventoryOpen == True and event.key == pygame.K_e:
                print('E pressed while in inv')
                screen.fill((0, 0, 0, 0))
                if imageIndex == 1:
                    clocksIteration = True
                imageList[imageIndex].draw()
                leftArrowButton.draw()
                rightArrow.draw()
                inventoryOpen = False
            else:
                print("E pressed")
                screen.fill((0, 0, 0, 0))
                inventoryBackground.draw()
                inventoryIcon.draw()
                inventoryIcon2.draw()
                inventoryHotbar.draw()
                inventoryOpen = True
                inventoryBorder = pygame.draw.rect(
                    screen, (0, 0, 0), pygame.Rect(197, 297, 300, 105), 2)
                inventoryTextThing.draw()
                try:
                    if inventory[0] == 'Key':
                        inventoryKey.draw()
                except:
                    print("The key has not been obtained yet.")

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos

            ##########################################################################################
            # General Info : pygame library gives you access to a method which takes in parameters left, top, width, height and returns a rectangle with coordinates based off of those nubmers. Rect(left, top, width, height) see more here under the top anwser which has a nice picture: https://stackoverflow.com/questions/22589322/what-does-top-left-right-and-bottom-mean-in-android-rect-object
            ##########################################################################################
            leftArrowRect = pygame.Rect(100, 200, 30, 30)
            rightArrowRect = pygame.Rect(540, 200, 30, 30)

            ##########################################################################################
            # Similar to the left arrow created a rectangle that (a reference to space within the screen), so that we can compare later the mouse click (x,y) corrdiantes and see if it matches anywhere near the button rectangle. Found these rectangle values by putting a print statment in the method called "draw()" within the Button.class, which our dialog button uses to be created, so it will be called and a break point will be hit. When it is hit on the left hand side I can see all the values for every button created and the info of each button like there dimensions. This is how I got the info.
            dialogButtonRect = pygame.Rect(1, 1, 64, 36)
            ##########################################################################################
            if leftArrowRect.collidepoint(x, y) or rightArrowRect.collidepoint(
                    x, y):
                inventoryOpen = False

            ##########################################################################################
            # The event given by the pygame library in the background when we click on the mouse somewhere on the screen, returns to us a position in (x,y) coordiantes. We will use this position to see if it matches the rectangle we created for the dialog button on the screen. Remember we reserved a rectanglar space on the screen with variable named "dialogButtonRect", which happens to be the exact place where the dialog button was drawn, and when we click on that space the points from the event and our rectangle will collide which will make the if statement below true and therefore drawing the dialog image using the Button.class method named "draw()". Side Note: remember the button variables (i.e. dialogButtonImageObject, dialogImageObject) that were created for the button image and dialog image that were using Button.class, or as you saw Button(self, x, y, scale), inherit all the methods within the class.
            if dialogButtonRect.collidepoint(x, y):
                dialogImageObject.draw()
            ##########################################################################################

            if menuScreen == True:
                if startButtonRect.collide(x, y):
                    print("it worked cool")

            if imageIndex == 1:
                clockRect = pygame.Rect(390, 40, 110, 110)
                leverRect = pygame.Rect(310, 175, 45, 45)
                keyRect = pygame.Rect(470, 215, 100, 110)
                if clockRect.collidepoint(x, y) and inventoryOpen == False:
                    print("Clock clicked")
                    if clockIndex == 11:
                        clockIndex = 0
                        clockTimes[clockIndex].draw()
                    else:
                        clockIndex += 1
                        clockTimes[clockIndex].draw()

                if leverRect.collidepoint(x, y) and inventoryOpen == False:
                    clockTimes[clockIndex].draw()
                    print("Lever clicked")
                    if leverState == False:
                        leverOn.draw()
                        leverState = True
                        if clockIndex == 4:
                            print("Correct!")
                            keyImageButton.draw()
                        else:
                            print("Don't you dare to guess again!")

                    elif leverState == True:
                        leverOff.draw()
                        leverState = False

                if keyRect.collidepoint(x, y) and inventoryOpen == False:
                    print("Key clicked")
                    screen.fill((0, 0, 0, 0))
                    imageOne = True
                    clocksIteration = True
                    inventory.append("Key")
                    inventory = list(set(inventory))
                    print(inventory)

            if inventoryOpen == True:
                slotOneRect = pygame.Rect(196, 296, 45, 56)
                if slotOneRect.collidepoint(x, y):
                    try:
                        print("In the first slot, there is a " + inventory[0])
                        keySelectedRect = pygame.draw.rect(
                            screen, (220, 20, 60), pygame.Rect(0, 0, 700, 700),
                            2)
                        keySelected = True
                    except:
                        print("There is nothing in that slot.")

pygame.quit()
