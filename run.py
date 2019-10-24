import pygame, sys
from pygame.locals import *
from classes import Screen, Player, Tile, Board, Piece

def start_game(player1, player2, player1color, player2color):
    screen = Screen(600, 60)
    screen.start_board_display()

    player1 = Player(player1, player1color)
    player1.initialize_pieces(screen)
    player2 = Player(player2, player2color)
    player2.initialize_pieces(screen)
    
    board = Board(screen)
    # board.draw()
    running = True
    while running:
        board.draw()
        player1.L5.draw()
        # print(player1.L5.piece_array)
        # board.draw()
        pygame.display.flip()       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

start_game("shawn","navi","blue","red")