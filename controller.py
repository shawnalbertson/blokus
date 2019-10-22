def board_array():
    board = []
    row = []
    for m in range(20):
        for n in range(20):
            row.append("w")
        board.append(row)
        row = []
    return board
