import pygame, sys
from pygame.locals import *

class Screen:
    def __init__(self, board_screen_width, board_screen_height, fps):
        """
        Initialize the screen dimension, and fps. Set the board's screen size.
        
        Arguments:
            board_screen_dimension : integer
                Number that is the height and width of the board screen

            fps : integer
                Frames per second
        """
        self.board_screen_width = board_screen_width
        self.board_screen_height = board_screen_height
        self.fps = fps
        self.board_screen = pygame.display.set_mode((self.board_screen_width, self.board_screen_height))

    def start_board_display(self):
        """
        Start the board display - only called once at the beginning of the game. Sets the program clock.
        """
        # Initialize pygame interface
        pygame.init()

        # Avoid copyright issues with convenient typos
        pygame.display.set_caption('Blockus')
        
        self.board_screen.fill((177,177,177))
        self.clock = pygame.time.Clock()

    def display_update(self, rect):
        """
        Updates the display by the fps set.
        """
        pygame.display.update(rect)
        self.clock.tick(self.fps)

class Tile:
    def __init__(self, Screen, tile_size, tile_x, tile_y, init_color):
        """
        Creates a tile objects and loads all of the tile images.

        Arguments:
            Screen : Pygame display
                The screen that you would like to display the tile on.
            
            Tile_size : integer
                Size of the tile width and tile height
            
            Tile_x : integer
                X location of the tile.
            
            Tile_y : integer
                Y location of the tile.
            
            Init_color : string
                Initial color of the tile.
        """
        
        self.tile_size = tile_size
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.screen = Screen

        # set the tiles to grey initially
        self.color_code = init_color

        # define a rectangle
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_size, self.tile_size)

        self.white = pygame.transform.scale(pygame.image.load("white.png").convert(), (self.tile_size, self.tile_size))
        self.green = pygame.transform.scale(pygame.image.load("green.png").convert(), (self.tile_size, self.tile_size))
        self.red = pygame.transform.scale(pygame.image.load("red.png").convert(), (self.tile_size, self.tile_size))
        self.yellow = pygame.transform.scale(pygame.image.load("yellow.png").convert(), (self.tile_size, self.tile_size))
        self.blue = pygame.transform.scale(pygame.image.load("blue.png").convert(), (self.tile_size, self.tile_size))

        self.prev_mouse_x = 0
        self.prev_mouse_y = 0
    def check_mouse_over(self, mouse_x, mouse_y):
        """
        Check if the mouse is over this tile's rectangle.
        
        Arguments:
            Mouse_x : float
                X coordinate of the mouse.
            
            Mouse_u : float
                Y coordinate of the mouse.
        """
        if self.rect.collidepoint(mouse_x,mouse_y):
            return True
        else:
            return False
    
    def colors(self):
        """
        Return the correct image to blit based on the color code.
        """
        if self.color_code == "w":
            return self.white
        elif self.color_code == "g":
            return self.green
        elif self.color_code == "r":
            return self.red
        elif self.color_code == "y":
            return self.yellow
        elif self.color_code == "b":
            return self.blue


    def draw_tile(self):
        """
        Blit the tile onto the screen.
        """
        self.screen.board_screen.blit(self.colors(), self.rect)
    
    def change_tile_location(self, mouse_x, mouse_y):
        """
        Based on mouse input change the starting point of the tile and create a rectangle for the image to blit to.

        Arguments:
            mouse_x : float
                Mouse's x location on the screen.
            
            mouse_y : float
                Mouse's y location on the screen.
        """

        self.tile_x = (self.tile_x - self.prev_mouse_x) + mouse_x
        self.tile_y = (self.tile_y - self.prev_mouse_y) + mouse_y
        self.prev_mouse_x = mouse_x
        self.prev_mouse_y = mouse_y
        self.rect = pygame.Rect(self.tile_x, self.tile_y, self.tile_size, self.tile_size)

class Board:
    def __init__(self, Screen):
        """
        Initialize the board on the board screen.

        Arguments:
            Screen : Pygame object
                Screen that the board should be blitted onto.

        Attributes:
            .rows : Integer 
                Number of rows, hard coded at 20
            .columns : Integer 
                Number of columns, hard coded at 20
            .tile_size : Integer
                Used as argument to Tile object, defined by number of rows and size of board
            .tiles : List of Tile objects

        Methods: 
            .draw() : Goes through list of Tile objects and draws them
            .modify_board(Piece, mouse_location) : Redefines board with new tiles
        """
        
        self.screen = Screen
        self.rows = 20
        self.columns = 20
        self.tile_size = 30
        self.board_size = self.tile_size * self.rows
        self.tiles = []

        self.board_offset_x = int((self.screen.board_screen_width/2)- (self.board_size/2))
        self.board_offset_y = int((self.screen.board_screen_height/2)- (self.board_size/2))

        # creating the tiles in a loop
        for row in range(0,self.rows):
            self.column = []
            for column in range(0,self.columns):
                self.tile = Tile(Screen, self.tile_size, row*self.tile_size + self.board_offset_x, column*self.tile_size + self.board_offset_y, 'w')
                self.column.append(self.tile)
                self.tile.draw_tile()
                
            self.tiles.append(self.column)

        self.board_rectangle = pygame.Rect(self.board_offset_x, self.board_offset_y, self.board_size, self.board_size)

    def draw(self):
        """
        Draw the board by parsing the list of Tile objects. 
        Because tile objects can draw themselves, call draw_tile 
        """
        for row, m in enumerate(self.tiles):
            for column, n in enumerate(m):
                n.draw_tile()  
    
    def modify_board(self, Piece, mouse_location):
        """
        Arguments:
            Piece : Piece object
            mouse_location : Tuple
                From pygame.mouse.get_mouse(), called in Piece.draw()
                
        """
        for row, m in enumerate(Piece):
            for column, n in enumerate(m):
                mouse_x = mouse_location[0]
                mouse_y = mouse_location[1]
                is_space_available = self.tiles[row + mouse_x][column + mouse_y].color_code
                if not n == "." and is_space_available == "w":
                    is_space_available = n
                elif not is_space_available == "w":
                    # change piece color to red version
                    pass
                else:
                    continue


class Piece(Board):

    def __init__(self, Screen, piece_array, color):
        """
        Initialize the piece object and create an array with the player's colors.

        Arguments:
            Screen : Pygame object
                Screen that you would like the piece to be drawn on.
            
            Piece_array : list
                List of strings that shows how the piece would be drawn.
            
            Color : string
                Player's click color.
        """
        super().__init__(Screen)
        self.piece_array = piece_array
        self.color = color
        self.screen = Screen
        self.is_used = 0
        for row, m in enumerate(self.piece_array):
            for column, n in enumerate(m):
                if not n == ".":
                    self.piece_array[row][column] = self.color
        
        self.this_tile = []
        for row, m in enumerate(self.piece_array):
            for column, n in enumerate(m):
                if n != '.':
                    self.this_tile.append(Tile(self.screen, self.tile_size, self.tile_size*row, self.tile_size*column, n))                      
                else:
                    continue 

          
    def rotate_piece(self):
        """
        Modify array such that the piece rotates.
        """
        pass
    
    def draw(self):
        if self.is_used == 0:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()

            # if mouse_x > self.board_coords[0][0] and mouse_x < self.board_coords[0][1] and mouse_y > self.board_coords[1][0] and mouse_y < self.board_coords[1][1]:

            for x in range(0,len(self.this_tile)):
                self.this_tile[x].change_tile_location(mouse_x, mouse_y)
                self.this_tile[x].draw_tile()

            if pygame.mouse.get_pressed()[0]:
                mouse_x = int(mouse_x/self.tile_size)
                mouse_y = int(mouse_y/self.tile_size)
                self.is_used = self.is_used + 1
                for x in range(0, len(self.this_tile)):
                    self.this_tile[x].change_tile_location(mouse_x*self.tile_size, mouse_y*self.tile_size)
                    self.this_tile[x].draw_tile
        
        else:
            for x in range(0, len(self.this_tile)):
                self.this_tile[x].draw_tile()
        
        

class Player:
    def __init__(self, player_name, player_color):
        """
        Initialize the player with what color their pieces should be and what their name is.

        Arguments:
            player_name : string
                Name of the player

            player_color : string
                Color that the pieces of the player are going to be
        """
        self.player_name = player_name
        self.player_color = player_color

        if self.player_color == "red":
            self.click_color = "r"
        if self.player_color == "blue":
            self.click_color = "b"
        if self.player_color == "green":
            self.click_color = "g"
        if self.player_color == "yellow":
            self.click_color = "y"
            
    def initialize_pieces(self, Screen):
        """
        Initializes all pieces objects for a player.
        
        Arguments:
            Screen : Pygame object
                Pygame screen object
        """
        # create all of the pieces and assign a used or not used to them
        self.V5 = Piece(Screen, [["x", "x", "x"], ["x",".","."], ["x",".","."]], self.click_color)
        self.plus = Piece(Screen, [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]], self.click_color)
        self.L5 = Piece(Screen, [["x", "x", "x", "x"], [".", ".", ".", "x"]], self.click_color)
        self.Y = Piece(Screen, [["x", "x", "x", "x"], [".", "x", ".", "."]], self.click_color)
        self.N = Piece(Screen, [["x", "x", "x", "."], [".", ".", "x", "x"]], self.click_color)
        self.U = Piece(Screen, [["x", ".", "x"], ["x", "x", "x"]], self.click_color)
        self.P = Piece(Screen, [["x", "x", "."], ["x", "x", "x"]], self.click_color)
        self.V3 = Piece(Screen, [["x", "."], ["x", "x"]], self.click_color)
        self.Z5 = Piece(Screen, [["x", "x", "."],[".", "x", "."], [".", "x" "x"]], self.click_color)
        self.Z4 = Piece(Screen, [["x", "x", "."], [".", "x", "x"]], self.click_color)
        self.T5 = Piece(Screen, [["x", "x", "x"], [".", "x", "."], [".", "x", "."]], self.click_color)
        self.S5 = Piece(Screen, [["x", "x", "x", "x", "x"]], self.click_color)
        self.S4 = Piece(Screen, [["x", "x", "x", "x"]], self.click_color)
        self.S3 = Piece(Screen, [["x", "x", "x"]], self.click_color)
        self.S2 = Piece(Screen, [["x", "x"]], self.click_color)
        self.S1 = Piece(Screen, [["x"]], self.click_color)
        self.L4 = Piece(Screen, [["x", ".", ".", "."], ["x", "x", "x", "x"]], self.click_color)
        self.square = Piece(Screen, [["x", "x"], ["x", "x"]], self.click_color)
        self.F = Piece(Screen, [[".", "x", "x"],["x", "x", "."], [".", "x", "."]], self.click_color)
        self.W = Piece(Screen, [["x", ".", "."], ["x", "x", "."], [".", "x", "x"]], self.click_color)
        self.T4 = Piece(Screen, [["x", "x", "x"], [".", "x", "."]], self.click_color)