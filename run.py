import pygame, sys
from pygame.locals import *
from classes import Screen, Player, Tile, Board, Piece

def start_game(player1, player2, player1color, player2color):
    screen = Screen(600, 40)
    screen.start_board_display()

    player1 = Player(player1, "green")
    player2 = Player(player2, "red")
    
    board = Board(screen)

    running = True
    while running:
        board.draw()
        screen.display_update()        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

start_game("shawn","navi","blue","red")