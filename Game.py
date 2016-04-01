# Game for Pip-Boy
# Imports
import pygame

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

smallFont = pygame.font.SysFont(None, 25)
mediumFont = pygame.font.SysFont(None, 50)
largeFont = pygame.font.SysFont(None, 75)
