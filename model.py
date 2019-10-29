import pygame

# Functions to load images
def piece_size(board_size, n):
    """
    
    Take board dimension and number of desired pieces per board
    Return the length of one edge of a tile as int type for pygame.transform.scale

    A regular Blokus board is 20x20
    """

    return int(board_size/n)



class Screen:
    def __init__(self, screen_size, fps):
        """
        Initialize the screen dimension, and fps. Set the board's screen size.
        
        Arguments:
            board_screen_dimension : integer
                Number that is the height and width of the board screen

            fps : integer
                Frames per second
        """
        self.screen_size = screen_size
        self.fps = fps
        self.board_screen = pygame.display.set_mode((self.screen_size, self.screen_size))

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
    """
        Includes color and size of tiles
        Reads image_file and makes it a scaled surface object
        Takes color_code for referring to different kinds of tiles
    """

    def __init__(self, image_file, size, color_code):
        im = pygame.image.load(image_file)
        self.image = pygame.transform.scale(im, (size, size))
        self.size = size
        self.color_code = color_code
    

class Tiles:
    """
        A more convenient way to store multiple tile objects that share information
        Pass in order white, green, red, yellow, blue
    """
    def __init__(self, tile1, tile2, tile3, tile4, tile5):
        self.tile1 = tile1
        self.tile2 = tile2
        self.tile3 = tile3
        self.tile4 = tile4
        self.tile5 = tile5
        self.size = tile1.size

class Board:
    """
        The object that contains all tile information

        Screen is a pygame surface object

        Tiles is an object with a few pre loaded tile images

        Array holds information about the colors of the board at the moment

        get_mouse determines if the image will follow your mouse or not
    """

    def __init__(self, screen, tiles, array, get_mouse = True):

        self.screen = screen
        self.size = tiles.size
        self.tiles = tiles

        # Define the five tile objects
        self.white = tiles.tile1.image
        self.green = tiles.tile2.image
        self.red = tiles.tile3.image
        self.yellow = tiles.tile4.image
        self.blue = tiles.tile5.image

    # If the input array is the string "board", draw the board array of 20x20 with white tiles
        if array == "board":
            board = []
            row = []
            for m in range(20):
                for n in range(20):
                    row.append("w")
                board.append(row)
                row = []
            self.array = board
        else:
            self.array = array
            
        self.get_mouse = get_mouse

    def draw(self):
        """
            Draw a piece or a board to screen object
            Don't draw anything that's not w, g, r, y or b
        """
        if self.get_mouse:
            (start_x, start_y) = pygame.mouse.get_pos()
        else:
            (start_x, start_y) = (0,0)
        
        # Go through every element in the array
        for i1, m in enumerate(self.array):
            for i2, n in enumerate(m):

                if n == "w":
                    self.screen.blit(self.white, (self.size*i2 + start_x, self.size*i1 + start_y))
                elif n == "g":
                    self.screen.blit(self.green, (self.size*i2 + start_x, self.size*i1 + start_y))
                elif n == "r":
                    self.screen.blit(self.red, (self.size*i2 + start_x, self.size*i1 + start_y))
                elif n == "y":
                    self.screen.blit(self.yellow, (self.size*i2 + start_x, self.size*i1 + start_y))
                elif n == "b":
                    self.screen.blit(self.blue, (self.size*i2 + start_x, self.size*i1 + start_y))                                                         
                else:
                    continue    
    
    def is_valid(self, modifier, start):
        """
            Decide if a move is valid before trying to place it
            Arguments:
                modifier : A piece object
                start : Tuple of mouse location as mapped to the 20x20 game board
        """
    # Go through each element in the array that defines modifier
        for row, m in enumerate(modifier.array):
            for column, n in enumerate(m):
    
    # Compare each board element with each piece element
                try:
                    check = self.array[row + start[1]][column + start[0]]

    # If the board element would overlap with an already filled board tile, return False               
                    if n != "." and check != "w":
                        return False

    # If the piece is out of range, return false rather than crash the program
                except IndexError:
                    return False

    # If the piece is within range and doesn't overlap an existing piece, is_valid returns True
        return True       

    def modify_board(self, modifier, start):
        """
            Change specific parts of board array to a new color
            Only called once the move has been checked for validity

            Arguments:
                modifier : Piece object
                start : Tuple of mouse location as mapped to the 20x20 game board
        """
    # Go through each element in the array that defines modifier
        for row, m in enumerate(modifier.array):
            for column, n in enumerate(m):

    # Alter the board array if array element n is a color
                if n != ".":
                    self.array[row + start[1]][column + start[0]] = n

    # Don't alter the board array if array element n is a blank
                elif n == ".":
                    pass

    # Once the code runs, the piece is made unavailable
        modifier.available = 0    



class Piece(Board):
    """
        The Piece class is very similar to Board because it is a compilation of tiles defined by an array
        It also has a condition that determines if the piece has already been played
    """
    def __init__(self, screen, tiles, array, available, get_mouse = True):
        super().__init__(screen, tiles, array, get_mouse)
        self.available = available

    def rotate_piece(self):
        """Modify array such that the piece rotates"""
        pass

    def assign_color(self, color):
        """
            Take in an array representing the shape of a piece
            Change the generic 'x' fill to one specific to a color
        """

    # Go through each element in the array
        for row, m in enumerate(self.array):
            for column, n in enumerate(m):
    
    # If the entry is not blank, change the color
                if not n == ".":
                    self.array[row][column] = color
    


class Player:
    """
    Initialize the player with what color their pieces should be and what their name is.

    Arguments:
        player_name : string
            Name of the player

        player_color : string
            Color that the pieces of the player are going to be
    """


    def __init__(self, player_name, player_color):
        """
            Defines player.click_color
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
            
    def initialize_pieces(self, Screen, Tiles, available = 1):
        """
        Initializes all pieces objects for a player.
        Makes a Piece object with array input, redefines the color with Piece.assign_color
        
        Arguments:
            Screen : Pygame object
                Pygame screen object

            Tiles : A class containing all the tiles

            available : The condition of whether or not the piece has been played
                1 when not yet played
                0 once played
        """
        self.available = available

        # create all of the pieces and assign a used or not used to them
        self.V5 = Piece(Screen, Tiles, [["x", "x", "x"], ["x",".","."], ["x",".","."]], self.available)
        self.V5.assign_color(self.click_color)

        self.V3 = Piece(Screen, Tiles, [["x", "x"], ["x","."]], self.available)
        self.V3.assign_color(self.click_color)        

        self.X = Piece(Screen, Tiles, [[".", "x", "."], ["x", "x", "x"], [".", "x", "."]], self.available)
        self.X.assign_color(self.click_color)
        
        self.N = Piece(Screen, Tiles, [[".", ".", "x", "x"], ["x", "x", "x", "."]], self.available)
        self.N.assign_color(self.click_color)

        self.L5 = Piece(Screen, Tiles, [["x", "x", "x", "x"], [".", ".", ".", "x"]], self.available)
        self.L5.assign_color(self.click_color)

        self.L4 = Piece(Screen, Tiles, [["x", "x", "x"], [".", ".", "x"]], self.available)
        self.L4.assign_color(self.click_color)

        self.Y = Piece(Screen, Tiles, [["x", "x", "x", "x"], [".", "x", ".", "."]], self.available)
        self.Y.assign_color(self.click_color)

        self.U = Piece(Screen, Tiles, [["x", ".", "x"], ["x", "x", "x"]], self.available)
        self.U.assign_color(self.click_color)  

        self.P = Piece(Screen, Tiles, [["x", "x", "."], ["x", "x", "x"]], self.available)
        self.P.assign_color(self.click_color)

        self.W = Piece(Screen, Tiles, [["x", "x", "."], [".", "x", "x"], [".", ".", "x"]], self.available)
        self.W.assign_color(self.click_color)

        self.F = Piece(Screen, Tiles, [["x", "x", "."], [".", "x", "x"], [".", "x", "."]], self.available)
        self.F.assign_color(self.click_color)      

        self.T5 = Piece(Screen, Tiles, [["x", "x", "x"], [".", "x", "."], [".", "x", "."]], self.available)
        self.T5.assign_color(self.click_color)          

        self.T4 = Piece(Screen, Tiles, [["x", "x", "x"], [".", "x", "."]], self.available)
        self.T4.assign_color(self.click_color)

        self.Z5 = Piece(Screen, Tiles, [["x", "x", "."], [".", "x", "."], [".", "x", "x"]], self.available)
        self.Z5.assign_color(self.click_color)

        self.Z4 = Piece(Screen, Tiles, [["x", "x", "."], [".", "x", "x"]], self.available)
        self.Z4.assign_color(self.click_color)

        self.S5 = Piece(Screen, Tiles, [["x", "x", "x", "x", "x"]], self.available)
        self.S5.assign_color(self.click_color)

        self.S4 = Piece(Screen, Tiles, [["x", "x", "x", "x"]], self.available)
        self.S4.assign_color(self.click_color)

        self.S3 = Piece(Screen, Tiles, [["x", "x", "x"]], self.available)
        self.S3.assign_color(self.click_color)

        self.S2 = Piece(Screen, Tiles, [["x", "x"]], self.available)
        self.S2.assign_color(self.click_color)

        self.S1 = Piece(Screen, Tiles, [["x"]], self.available)
        self.S1.assign_color(self.click_color)

        self.square = Piece(Screen, Tiles, [["x", "x"], ["x", "x"]], self.available)
        self.square.assign_color(self.click_color)
        
    def choose_piece(self, event_key):
        """
            Associates each piece with a keyboard stroke
            Returns false if the input does not associate with any piece

            Arguments:
                event_key : pygame result specifically from a pygame.KEYDOWN event
        """

        if event_key == pygame.K_q:
            return self.V5
        elif event_key == pygame.K_w:
            return self.V3
        elif event_key == pygame.K_e:
            return self.X    
        elif event_key == pygame.K_r:
            return self.N 
        elif event_key == pygame.K_t:
            return self.L5
        elif event_key == pygame.K_i:
            return self.L4
        elif event_key == pygame.K_y:
            return self.Y
        elif event_key == pygame.K_u:
            return self.U
        elif event_key == pygame.K_p:
            return self.P
        elif event_key == pygame.K_o:
            return self.W
        elif event_key == pygame.K_f:
            return self.F
        elif event_key == pygame.K_s:
            return self.T5
        elif event_key == pygame.K_d:
            return self.T4
        elif event_key == pygame.K_a:
            return self.Z5
        elif event_key == pygame.K_g:
            return self.Z4
        elif event_key == pygame.K_h:
            return self.S5
        elif event_key == pygame.K_j:
            return self.S4
        elif event_key == pygame.K_k:
            return self.S3
        elif event_key == pygame.K_l:
            return self.S2
        elif event_key == pygame.K_z:
            return self.S1
        elif event_key == pygame.K_x:
            return self.square
        else:
            return False

        