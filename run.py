import pygame, sys
from pygame.locals import *
from classes import Screen, Player, Tile, Board, Piece

def start_game(player1, player2, player3, player4, player1color, player2color, player3color, player4color):
    screen = Screen(900,900, 90)
    screen.start_board_display()

    player1 = Player(player1, player1color)
    player1.initialize_pieces(screen)
    player2 = Player(player2, player2color)
    player2.initialize_pieces(screen)
    player3 = Player(player3, player3color)
    player3.initialize_pieces(screen)
    player4 = Player(player4, player4color)
    player4.initialize_pieces(screen)
    
    board = Board(screen)
    # board.draw()
    running = True
    
    while running:
        board.draw()
        player1.L5.draw()
        screen.display_update(board.board_rectangle)
        pygame.display.update(board.board_rectangle)       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

start_game("shawn","navi", "ben", "hill", "blue","red", "green", "yellow")