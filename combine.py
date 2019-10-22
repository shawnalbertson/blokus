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

        self.clock = pygame.time.Clock()
    
    def display_update(self):
        pygame.display.update()
        self.clock.tick(30)



class Player:
    def __init__(self, player_name, player_color):
        self.player_name = player_name
        self.player_color = player_color

        if self.player_color == "red":
            self.click_color = (255, 0, 0)
        if self.player_color == "blue":
            self.click_color = (0, 0, 255)
        if self.player_color == "green":
            self.click_color = (0, 255, 0)
        if self.player_color == "yellow":
            self.click_color = (247, 255, 0)