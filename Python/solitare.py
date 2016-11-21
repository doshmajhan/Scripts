import sys

def make_board(size):
    board =  [[' ' for x in range(size)] for x in range(size)]
    for x in range(size):
        if x < 2 or x > 4:
            for i in range(2, 5):
                board[x][i] = "x"
            board[x][1] = "|"
            board[x][5] = "|"
        else:
            for i in range(size):
                board[x][i] = "x"
    board[3][3] = " "
    return board

def print_board(board, size):
    print("  ", end="")
    for x in range(size):
        print(x, end="\t")
    print("\n")
    print("\t+-------------------------------+")
    for x in range(size):
        print(x, end=" ")

        if x == 1 or x == 5:
            print("+-----------+", end=" ")
            for i in range(2, 5):
                print(board[x][i], end="\t")
            print("+-----------+", end=" ")
        else:
            if x > 1 and x < 5:
                print("|", end="\t")

            for i in range(size):
                print(board[x][i], end="\t")

            if x > 1 and x < 5:
                print("|")

        print("\n")
    print("\t+-------------------------------+")


def is_valid(row, col, check):
    if (row < 0 or row > 6) or (col < 0 or col > 6):
        print("Illegal location.")
        return False

    if (row < 2  or row > 4) and (col < 2 or col > 4):
        print("Illegal location.")
        return False

    if check:
        if board[row][col] != "x":
            print("Illegal move, no peg at source location.")
            return False

    else:
        if board[row][col] == "x":
            print("Illegal move, destination location is occupied.")
            return False

    return True

def check_move(row1, col1, row2, col2, board):
    if row1 == row2:
        if (col1-col2) != 2:
            print("Illegal move, can only jump over one peg, re-enter move.")
            return False

        elif col1 < col2:
            if board[col1+1] != 'x':
                print("Illegal move, no peg being jumped over, re-enter move.")
                return False

        else:
            if board[col1-1] != 'x':
                print("Illegal move, no peg being jumped over, re-enter move.")
                return False

    elif col1 == col2:
        if (row1-row2) != 2:
            print("Illegal move, can only jump over one peg, re-enter move.")
            return False

        elif row1 < row2:
            if board[row1+1] != 'x':
                print("Illegal move, no peg being jumped over, re-enter move.")
                return False

        else:
            if board[row1-1] != 'x':
                print("Illegal move, no peg being jumped over, re-enter move.")
                return False

    else:
        print("Illegal move.")

    return True

def make_move(row1, row2, col1, col2, board):
    board[row1][col1] = ""
    board[row2][col2] = "x"
    if row1 == row2:
        if col1 < col2:
            board[row1][col+1] = ""
        else:
            board[row1][col-1] = ""
    else:
        if row1 < row2:
            board[row1+1][col1] = ""
        else:
            board[row1-1][col1] = ""

def check_remaining(board, size):
    for x in range(size-3):
        for i in range(size-3):
            if is_valid(x, i, True):
                if is_valid(x+2, i, False):
                    if check_move(x, i, x+2, i, board):
                        return True

                elif is_valid(x, i+2, False):
                    if check_move(x, i, x, i+2, board):
                        return True

            elif is_valid(x, i+2, True):
                if is_valid(x, i, False):
                    if check_move(x, i+2, x, i, board):
                        return True

            elif is_valid(x+2, i, True):
                if is_valid(x, i, False):
                    if check_move(x+2, i, x, i, board):
                        return True

    return False


if __name__ == '__main__':
    size = 7
    board = make_board(size)
    print_board(board, size)
    while True:
        peg1 = int(input("Enter the location of the peg to move (RC, -1 to quit):
"))
        row1 = peg1/10
        col1 = peg1%10

        check = is_valid(row1, col1, True)
        if not check:
            continue

        if peg1 == -1:
            print("Player quit.")
            sys.exit()

        peg2 = int(input("Enter the location where the peg is moving to (RC, -1 to quit):"))
        row2 = peg2/10
        col2 = peg2%10

        check = is_valid(row2, col2, False)
        if not check:
            continue

        if peg2 == -1:
            print("Player quit.")
            sys.exit()

    count = 0
    for x in range(size):
        for i in range(size):
            if board[x][i] == "x":
                count += 1
    print("You left %d pegs on board" % count)
