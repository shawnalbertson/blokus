"""
    This script includes all the functions specific to defining a single user's turn
    It uses classes defined in model.py
"""

import pygame
import time

from blockus_components import *

def load(screen_dim, screen_fps, f1, f2, f3, f4, f5, f6):
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
    global gray
    global tiles
    global board
    # global every_piece_image

    # Initialize screen
    screen = Screen(screen_dim, screen_fps)
    screen.start_board_display()
    
    # Initialize size of one piece
    size = piece_size(screen.screen_size, 20)

    # Load image files as Tile objects
    white = Tile(f1, size, ".")
    green = Tile(f2, size, "g")
    red = Tile(f3, size, "r")
    yellow = Tile(f4, size, "y")
    blue = Tile(f5, size, "b")
    gray = Tile(f6, size, "v")

    # Add tiles to a single class
    tiles = Tiles(white, green, red, yellow, blue, gray)

    # Make a board
    # The array input -> "board" is a special case that creates a 20x20 'w' array
    board = Board(screen.board_screen, tiles, "board", False)

def one_status(input, coords, screen):
    """

    """
    font = pygame.font.Font('Helvetica.ttf', 16) 
    if input == "Available":
        text = font.render(input, True, (0,0,0), (0, 255, 0))
    else:
        text = font.render(input, True, (0,0,0), (255, 0, 0))

    textRect = text.get_rect()  
    textRect.center = coords
    screen.board_screen.blit(text, textRect)


def draw_status(player, screen):
    status_list = player.get_played_status()

    one_status(status_list[0], (110, 110), screen)
    one_status(status_list[1], (220, 110), screen)
    one_status(status_list[2], (335, 110), screen)
    one_status(status_list[3], (465, 110), screen)
    one_status(status_list[4], (50, 235), screen)
    one_status(status_list[5], (160, 235), screen)
    one_status(status_list[6], (290, 235), screen)
    one_status(status_list[7], (425, 235), screen)
    one_status(status_list[8], (540, 235), screen)
    one_status(status_list[9], (70, 415), screen)
    one_status(status_list[10], (180, 415), screen)
    one_status(status_list[11], (275, 415), screen)
    one_status(status_list[12], (380, 415), screen)
    one_status(status_list[13], (480, 415), screen)
    one_status(status_list[14], (560, 415), screen)
    one_status(status_list[15], (50, 585), screen)
    one_status(status_list[16], (130, 585), screen)
    one_status(status_list[17], (220, 585), screen)
    one_status(status_list[18], (320, 585), screen)
    one_status(status_list[19], (420, 585), screen)
    one_status(status_list[20], (530, 585), screen)

def place_piece(event_key, player, board, screen):
    """
        This function checks to see if a player's piece is available

        If it is, it draws the piece and waits for the input that would allow it to modify the board

        If not, it waits for a valid piece
    """

    if event_key == pygame.K_c:

        piece = player.choose_piece(event_key)
        draw = True
        while draw:
            piece.draw()
            
            every_piece_image = pygame.transform.scale(pygame.image.load("all_tiles.png"), (550, 550))
            screen.board_screen.blit(every_piece_image, (25, 25))
            draw_status(player, screen)
            pygame.display.flip()

            for event in pygame.event.get():
                
                # Close the game whenever the x is hit
                if event.type == pygame.QUIT:
                    pygame.quit()            

                if event.type == pygame.KEYDOWN:
                    place_piece(event.key, player, board, screen)
                    draw = False
    
    else:
        piece = player.choose_piece(event_key)


    # Only run this if piece.available is True
    # piece.available is instantiated at 1 at the time of creating pieces
        if piece.available:

        # Draw status is True to start
            draw = True

        # Draw the piece wherever the mouse is while the player chooses the piece location
            while draw:
                board.draw()
                piece.draw()

        # Now go through the logic of detecting a click and placing the piece accordingly
                for event in pygame.event.get():

        # Close the game whenever the x is hit
                    if event.type == pygame.QUIT:
                        pygame.quit()

        # Rotate the piece if there's a left input
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            piece.array = piece.rotate_piece()
                            continue

        # Flip the piece if there's a right input
                        if event.key == pygame.K_RIGHT:
                            piece.array = piece.flip_piece()
                            continue



        # Detect a mouse click event, snap mouse location to nearest integer
                    if pygame.mouse.get_pressed()[0]:
                        mouse_x, mouse_y = event.pos
                        mouse_x = int(mouse_x/size)
                        mouse_y = int(mouse_y/size)

        # Run board.is_valid to see if the move is valid
                        if board.is_valid(piece, (mouse_x, mouse_y)):    

        # If the move is valid, call modify_board to make changes to the board                   
                            board.modify_board(piece, (mouse_x, mouse_y))

        # If the move is not valid, call place_piece again with the inputs from your_turn
        # Effectively, an invalid move restarts the move choice process and nothing happens
                        else:
                            place_piece(event_key, player, board, screen)
                            # your_turn(player, board, screen)

        # Once the piece is placed, change draw condition to False
                        draw = False

        # Another possible event is for another key to get clicked
        # If so, choose a new piece with player.choose_piece
        # Call place_piece with the new piece input
                    if event.type == pygame.KEYDOWN:
                        # piece = player.choose_piece(event.key)
                        place_piece(event.key, player, board, screen)

        # Once the piece is placed, change draw condition to False
                        draw = False

        # Update the display after going through to check the conditions of the piece
                    pygame.display.flip()

        # If the piece has been played, call your_turn again so you don't go on the next player yet
        else:
            print("You already played this piece!")
            your_turn(player, board, screen)

def your_turn(player, board, screen):
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

    # Update the entire board each time through the while loop
        pygame.display.flip()
    
    # Get pygame events
    # End the game if the x is hit
    # Otherwise wait for a pygame.KEYDOWN event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    # Detect keyboard input
            if event.type == pygame.KEYDOWN:

    # Only run this section of code if the keyboard input actually correlates to a piece
    # This works because player.choose_piece() returns False if the key stroke does NOT correlate to a piece
                if player.choose_piece(event.key):

    # Choose a piece
                    # piece = player.choose_piece(event.key)

    # Call place_piece go through the process of placing a piece on the board
                    place_piece(event.key, player, board, screen)

    # Once the piece has been successfully played, running = False and the turn is over
                    running = False

    # If the keyboard input is not valid, pass and continue to wait for a valid input
                else:
                    pass

def play(p1, p2, p3, p4, p1color, p2color, p3color, p4color, screen):
    """
        Initialize players and pieces
        Run a cycle so that each player gets a turn, one after the other
    """

    # Initialize four players from the function input
    p1 = Player(p1, p1color)
    p1.initialize_pieces(screen.board_screen, tiles)
    p2 = Player(p2, p2color)
    p2.initialize_pieces(screen.board_screen, tiles)
    p3 = Player(p3, p3color)
    p3.initialize_pieces(screen.board_screen, tiles)
    p4 = Player(p4, p4color)
    p4.initialize_pieces(screen.board_screen, tiles)


    # turn_counter is used as a way to cycle through the pieces
    turn_counter = 0

    # Each integer 0->3 corresponds to a certain player's turn
    # Once a turn is over, go to the next player's turn

    while True:
        if turn_counter == 0:

            your_turn(p1, board, screen)
            turn_counter += 1

        if turn_counter == 1:

            your_turn(p2, board, screen)
            turn_counter += 1

        if turn_counter == 2:

            your_turn(p3, board, screen)
            turn_counter += 1

        if turn_counter == 3:

            your_turn(p4, board, screen)    
            turn_counter = 0


# Instantiate globals including a screen, tiles, and a board
load(600, 60, "white.png", "green.png", "red.png", "yellow.png", "blue.png", "gray.jpg")

# Play the game with some fun people
play("shawn", "navi", "ben", "hill", "blue", "green", "red", "yellow", screen)