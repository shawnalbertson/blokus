# Function to draw a board with white tile pieces to start


class Board:
    """ The object that contains all tile information
    """


    def __init__(self):
        self.board = []
        self.row = []
        for m in range(20):
            for n in range(20):
                self.row.append(".")
            self.board.append(self.row)
            self.row = []
            
    def make_board(self):
        """Define board for optional input conditions. 
        All periods means a base board

        base tile = "."
        green tile = "g"
        blue tile = "b"
        red tile = "r"
        yellow tile = "y"
        """
        
        for i1, m in enumerate(self.board):
            for i2, n in enumerate(m):
                # print((i1, i2), n)
                if n == "."
                    screen.blit(white, (size*i1, size*i2))


b = Board()
print(b.make_board())