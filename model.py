import pygame

# Functions to load images
def piece_size(board_size, n):
    """Take board dimension and number of desired pieces per board
    Return the length of one edge of a tile as int type for pygame.transform.scale

    A regular Blokus board is 20x20
    """
    # if a tuple:
    # return int(min(board_size)/n)
    # if a single number
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
    """Includes color and size of tiles
    Reads image_file and makes it a scaled surface object
    Takes size found in main script
    Takes color_code for referring to different kinds of tiles
    """

    def __init__(self, image_file, size, color_code):
        im = pygame.image.load(image_file)
        self.image = pygame.transform.scale(im, (size, size))
        self.size = size
        self.color_code = color_code
    

class Tiles:
    """A more convenient way to store multiple tile objects that share information
    pass in order white, green, red, yellow, blue
    """
    def __init__(self, tile1, tile2, tile3, tile4, tile5):
        self.tile1 = tile1
        self.tile2 = tile2
        self.tile3 = tile3
        self.tile4 = tile4
        self.tile5 = tile5
        self.size = tile1.size

class Board:
    """ The object that contains all tile information

    Screen is a pygame surface object

    Tiles is an object with a few pre loaded tile images

    Array holds information about the colors of the board at the moment

    get_mouse determines if the image will follow your mouse or not
    """

    def __init__(self, screen, tiles, array, get_mouse = True):

        self.screen = screen
        self.size = tiles.size
        self.tiles = tiles

        # Make color images
        self.white = tiles.tile1.image
        self.green = tiles.tile2.image
        self.red = tiles.tile3.image
        self.yellow = tiles.tile4.image
        self.blue = tiles.tile5.image

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
        """Draw a piece or a board to screen object
        Don't draw anything that's not w, g, r, y or b
        """
        if self.get_mouse:
            (start_x, start_y) = pygame.mouse.get_pos()
        else:
            (start_x, start_y) = (0,0)
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
    


    def modify_board(self, modifier, start):
        """Rewrite certain chunks of array to a new color

        Used to change the big board over time

        modifier is another Board object that should relate to a piece
            contains colors
        
        start is a tuple relating to the current mouse location
            a.k.a where the piece is going to be dropped

        This is where snapping will come into play, because the mouse should get moved to a particular location for placing the piece

        This is a good place to check that the piece fits on the board in the first place
        """
        # A list to fill with the tiles that have already been drawn on 
        current_write= []

        for row, m in enumerate(modifier.array):
            current_write.append([])
            for column, n in enumerate(m):
                check = self.array[row + start[1]][column + start[0]]
                
                # The case where the piece array is getting drawn to the board array
                if n != "." and check == "w":
                    self.array[row + start[1]][column + start[0]] = n

                    current_write[row].append(check)

                # A blank in the piece array
                elif n == ".":
                    current_write[row].append(check)

                # The case where a collision is detected
                elif n != "." and check != "w":
                    self.reset = Piece(self.screen, self.tiles, current_write, 1)
                    self.reset_play(self.reset, start)
                    return

    def reset_play(self, modifier, start):
        """
            If a play is invalid, this changes the board back to where it would have been before the play
        """
        for row, m in enumerate(modifier.array):
            for column, n in enumerate(m):
                self.array[row + start[1]][column + start[0]] = n


class Piece(Board):

    def __init__(self, screen, tiles, array, available, get_mouse = True):
        super().__init__(screen, tiles, array, get_mouse)
        self.available = available

    def rotate_piece(self):
        """Modify array such that the piece rotates"""
        pass

    def assign_color(self, color):
        """Take in a general array representing a piece
        Assign the general fill with the newly definied fill
        """

        #THIS IS CORRECT FOR COLOR ASSIGNMENT
        for row, m in enumerate(self.array):
            for column, n in enumerate(m):
                if not n == ".":
                    self.array[row][column] = color
    


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
            
    def initialize_pieces(self, Screen, Tiles, available = 1):
        """
        Initializes all pieces objects for a player.
        
        Arguments:
            Screen : Pygame object
                Pygame screen object
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
        
