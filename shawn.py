"""
    This script includes all the functions specific to defining a single user's turn
    It uses classes defined in model.py
"""

import pygame
import time

from model import *

def load(screen_dim, screen_fps, f1, f2, f3, f4, f5):
    """
        Runs the tasks that only need to be called once
        Creates global variables which only exist in this script

        Arguments:

        screen_dim and screen_fps are used as input to initialize Screen object

        f1, f2, f3, f4, f5 are the strings of the file names associated with tile images
    """

    global screen
    global size
    global white
    global green
    global red
    global yellow
    global blue
    global tiles
    global board

    # Initialize screen
    screen = Screen(screen_dim, screen_fps)
    
    # Initialize size of one piece
    size = piece_size(screen.screen_size, 20)

    # Load image files as Tile objects
    white = Tile(f1, size, ".")
    green = Tile(f2, size, "g")
    red = Tile(f3, size, "r")
    yellow = Tile(f4, size, "y")
    blue = Tile(f5, size, "b")

    tiles = Tiles(white, green, red, yellow, blue)

    board = Board(screen.board_screen, tiles, "board", False)


def place_piece(player, board, piece):
    """
        This function checks to see if a player's piece is available

        If it is, it draws the piece and waits for the input that would allow it to modify the board

        If not, it waits for a valid piece
    """
    if piece.available:
        draw = True

        while draw:
            board.draw()
            piece.draw()

# Now go through the logic of detecting a click and placing the piece accordingly
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if pygame.mouse.get_pressed()[0]:
                    # snap to the integer position
                    mouse_x, mouse_y = event.pos
                    mouse_x = int(mouse_x/size)
                    mouse_y = int(mouse_y/size)

# Modify_board does the work of changing the board array
                    if board.is_valid(piece, (mouse_x, mouse_y)):                       
                        board.modify_board(piece, (mouse_x, mouse_y))
                    else:
                        place_piece(player, board, piece)

                    draw = False

                if event.type == pygame.KEYDOWN:
                    piece = player.choose_piece(event.key)
                    place_piece(player, board, piece)
                    draw = False

                pygame.display.flip()

    else:
# If the piece has been played, call your_turn again so you don't go on the next player yet
        print("You already played this piece!")
        your_turn(player, board)

def your_turn(player, board):
    """
        Takes a player and a board, waits for keyboard input
        Uses choose_piece to associate a click with a piece
        Uses place_piece to put a piece on the board
    """

    # Establish a running status called 'running'
    running = True
    while running:
    # Draw the board first to establish the "waiting" period before a piece is selected
        board.draw()
        pygame.display.flip()
    
    # Give the option to close the window in this phase
        for event in pygame.event.get():
            # First layer to choose a piece
            if event.type == pygame.QUIT:
                pygame.quit()

    # Once keyboard input is detected, enter a new part of the code with running status called 'draw'
            if event.type == pygame.KEYDOWN:

                # piece = choose_piece(player, event.key)
                piece = player.choose_piece(event.key)

                place_piece(player, board, piece)
                # piece.available = 0
                running = False

def play(p1, p2, p3, p4, p1color, p2color, p3color, p4color):
    """
        Initialize players and pieces
    """

    p1 = Player(p1, p1color)
    p1.initialize_pieces(screen.board_screen, tiles)
    p2 = Player(p2, p2color)
    p2.initialize_pieces(screen.board_screen, tiles)
    p3 = Player(p3, p3color)
    p3.initialize_pieces(screen.board_screen, tiles)
    p4 = Player(p4, p4color)
    p4.initialize_pieces(screen.board_screen, tiles)


    turn_counter = 0
    # start by choosing your piece

    while True:
        if turn_counter == 0:

            your_turn(p1, board)
            turn_counter += 1

        if turn_counter == 1:

            your_turn(p2, board)
            turn_counter += 1

        if turn_counter == 2:

            your_turn(p3, board)
            turn_counter += 1

        if turn_counter == 3:

            your_turn(p4, board)    
            turn_counter = 0

 
load(600, 60, "white.png", "green.png", "red.png", "yellow.png", "blue.png")

play("shawn", "navi", "ben", "hill", "blue", "green", "red", "yellow")
