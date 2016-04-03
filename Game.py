# Game for Pip-Boy
# Imports
import pygame
import random

# Initialise PyGame
pygame.init()

# Set display width and height
display_width = 500
display_height = 500

# Create a gameDisplay using display_width and display_height
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set the caption of the window to Turret Defense
pygame.display.set_caption('Tanks')

# Create colours using RGB values
black = (0, 0, 0)
green = (0, 150, 0)
lightGreen = (0, 255, 0)

# Create fonts
smallFont = pygame.font.SysFont(None, 25)
mediumFont = pygame.font.SysFont(None, 50)
largeFont = pygame.font.SysFont(None, 75)

# Initialise the clock for FPS
clock = pygame.time.Clock()

# Tank part dimensions
tankWidth = 40
tankHeight = 20
turretWidth = 5
wheelWidth = 5


def text_objects(text, color, size="smallFont"):  # Function returns text for blitting
    if size == "smallFont":
        textSurface = smallFont.render(text, True, color)
    if size == "mediumFont":
        textSurface = mediumFont.render(text, True, color)
    if size == "largeFont":
        textSurface = largeFont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="smallFont"):  # Blits text to button
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + buttonwidth/2), buttony + (buttonheight/2))
    gameDisplay.blit(textSurface, textRect)


def message_to_screen(msg, color, y_displace=0, size= "smallFont"):  # Blits the text returned from text_objects
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurface, textRect)


def tank(x, y, turretPosition):
    # Casting x and y to be ints
    x = int(x)
    y = int(y)

    # Set possible turret positions
    turrets = [(x - 27, y - 2),
               (x - 26, y - 5),
               (x - 25, y - 8),
               (x - 23, y - 12),
               (x - 20, y - 14),
               (x - 18, y - 15),
               (x - 15, y - 17),
               (x - 13, y - 19),
               (x - 11, y - 21)]

    # Draw the tank
    pygame.draw.circle(gameDisplay, green, (int(x), int(y)), 10)
    pygame.draw.rect(gameDisplay, green, (x - tankHeight, y, tankWidth, tankHeight))
    pygame.draw.line(gameDisplay, green, (x, y), turrets[turretPosition], turretWidth)

    pygame.draw.circle(gameDisplay, green, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 0, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, green, (x + 15, y + 20), wheelWidth)


def barrier(xLocation, yLocation):  # Draw the barrier
    pygame.draw.rect(gameDisplay, green, [xLocation, display_height - yLocation, 50, yLocation])


def game_controls():  # Function for controls screen
    controls = True

    while controls:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Controls!", green, -100, size="largeFont")
        message_to_screen("Left and right arrow keys to move the tank!", green, 10, size="smallFont")
        message_to_screen("Up and down arrow keys to move the tank's turret!", green, 40, size="smallFont")
        message_to_screen("Controls!", green, 70, size="smallFont")
        message_to_screen("P to pause the game!", green, 100, size="smallFont")

        # Buttons
        button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def button(text, x, y, width, height, colour, active_colour, action):  # Creates the button, both active and inactive
    cursor = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > cursor[0] > x and y + height > cursor[1] > y:
        pygame.draw.rect(gameDisplay, active_colour, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "play":
                gameLoop()

            if action == "controls":
                game_controls()

            if action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, colour, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


def pause():  # Pauses the game
    paused = True
    message_to_screen("Paused", green, -100, size="largeFont")
    message_to_screen("C to continue playing", green, 50, size="smallFont")
    message_to_screen("Q to quit", green, 75, size="smallFont")
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        clock.tick(5)


def game_intro():  # Function for game introduction screen

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("Tanks!", green, 0, size="largeFont")

        # Text on the buttons
        button("Play", 25, 400, 100, 50, green, lightGreen, action="play")
        button("Controls", 200, 400, 100, 50, green, lightGreen, action="controls")
        button("Quit", 375, 400, 100, 50, green, lightGreen, action="quit")

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    # Tank positioning
    mainTankX = display_width * .8
    mainTankY = display_height * .8
    tankMove = 0
    curTurretPosition = 0
    changeTurretPosition = 0

    # Barrier positioning
    xLocation = (display_width/2) + random.randint(-.1 * display_width, .1 * display_width)
    yLocation = random.randrange(display_height * .2, display_height * .5)

    while not gameExit:

        if gameOver == True:
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Movement for tank
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTurretPosition = 1

                elif event.key == pygame.K_DOWN:
                    changeTurretPosition = -1

                elif event.key == pygame.K_p:
                    pause()

            # If user stops pressing the button, stop moving the tank
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTurretPosition = 0

        # Draw the game screen
        gameDisplay.fill(black)
        mainTankX += tankMove

        # Draw the barrier
        barrier(xLocation, yLocation)

        # Turret positioning
        curTurretPosition += changeTurretPosition
        if curTurretPosition > 8:
            curTurretPosition = 8
        elif curTurretPosition < 0:
            curTurretPosition = 0

        tank(mainTankX, mainTankY, curTurretPosition)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
