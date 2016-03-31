import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((800, 600))
gameDisplay.fill(black)

while True:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            pygame.quit()
            quit()

    pygame.display.update()