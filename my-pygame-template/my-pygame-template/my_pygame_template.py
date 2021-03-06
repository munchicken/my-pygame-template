#my pygame template

#imports
import pygame

#initilize game engine
pygame.init()

#constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#initilize display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  #moved this to game class last time
pygame.display.set_caption("My Pygame Template")  #moved this to game class last time

#initialize game variables
is_game_over = False  #moved this to game class last time, in game loop method

#game loop
#moved this to game class last time, in game loop method
while not is_game_over:

    #event handler
    for event in pygame.event.get():
        #game quit
        if event.type == pygame.QUIT:
            is_game_over = True

        #update display
        pygame.display.update()

#quit game
pygame.quit()
