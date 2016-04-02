# Game for Pip-Boy
# Imports
import pygame
import time

# Initialise PyGame
pygame.init()

# Set display width and height
display_width = 500
display_height = 500

# Create a gameDisplay using display_width and display_height
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Set the caption of the window to Turret Defense
pygame.display.set_caption('Turret Defense')

# Create colours using RGB values
black = (0, 0, 0)
green = (0, 255, 0)

# Create fonts
smallFont = pygame.font.SysFont(None, 25)
mediumFont = pygame.font.SysFont(None, 50)
largeFont = pygame.font.SysFont(None, 75)

# Initialise the clock for FPS
clock = pygame.time.Clock()


def game_intro():  # Function for game introduction screen

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        intro = False

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        gameDisplay.fill(black)

        pygame.display.update()

game_intro()


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    while not gameExit:

        if gameOver == True:
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:

                            gameExit = True
                            gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # Pass acts as a place holder until buttons are used
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass

                elif event.key == pygame.K_RIGHT:
                    pass

                elif event.key == pygame.K_UP:
                    pass

                elif event.key == pygame.K_DOWN:
                    pass

        gameDisplay.fill(black)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop()


def pause():
    paused = True
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


def text_objects(text, color, size="smallFont"):
    if size == "smallFont":
        textSurface = smallFont.render(text, True, color)
    if size == "mediumFont":
        textSurface = mediumFont.render(text, True, color)
    if size == "largeFont":
        textSurface = largeFont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace=0, size= "smallFont"):
    textSurface, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurface, textRect)