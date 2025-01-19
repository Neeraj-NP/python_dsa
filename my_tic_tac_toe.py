
board = [[' ' for i in range(3)] for j in range(3)]


def print_board():
    for row in board:
        print(row)


def place_mark(mark, position):
    row = position // 10 - 1 
    col = position % 10 - 1   
    if row in range(3) and col in range(3): 
        board[row][col] = mark
    else:
        print("Invalid position!")

place_mark('0', 31) 
print_board()
