import pygame, sys
from pygame.locals import *

class Screen:
    def __init__(self, screen_width, screen_height, fps):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps

    def start_display(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))

        # Avoid copyright issues with convenient typos
        pygame.display.set_caption('Blockus')

class Tile:
    def __init__(self, Screen, tile_width, tile_height, tile_x, tile_y, Player):
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_x = tile_x
        self.tile_y = tile_y

        # set the tiles to grey initially
        self.color = (177,177,177)

        if player.color == "red":
            self.click_color = (255, 0, 0)
        if player.color == "blue":
            self.click_color = (0, 0, 255)
        if player.color == "green":
            self.click_color = (0, 255, 0)
        if player.color == "yellow":
            self.click_color = (247, 255, 0)
        
        # define a rectangle
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_width, self.tile_height)
        
        # draw the rectangle
        pygame.draw.rect(screen.screen, self.color, self.rect, width = 3)

    def check_mouse_over(self, mouse_x, mouse_y):
        if 


class Player:
    def __init__(self, player_name, player_color):
        self.player_name = player_name
        self.player_color = player_color


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                if mouseOver:
                    # Change the current color if button was clicked.
                    button_color = AFTERCLICK

        mouseOver = determine_mouseOver(mousex, mousey)

        DISPLAYSURF.fill(BGCOLOR)
        # Just draw the rect with the current button color.
        pygame.draw.rect(DISPLAYSURF, button_color, myRectangle)

        if mouseOver:
            pygame.draw.rect(DISPLAYSURF, AFTERCLICK, myRectangle, 3)

        pygame.display.update()
        FPSCLOCK.tick(30)

def determine_mouseOver(valx, valy):
    if myRectangle.collidepoint(valx, valy):
        return True
    else:
        return False

main()
