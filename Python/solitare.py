import sys
s
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
    if check:
        if (row < 0 or row > 6) or (col < 0 or col > 6):
            print("Illegal location.")
            sys.exit()

        elif board[row][col] != "x":
            print("Illegal move, no peg at source location.")
            sys.exit()
    else:
        if (row < 0 or row > 6) or (col < 0 or col > 6):
            print("Illegal location.")
            sys.exit()

        elif board[row][col] == "x":
            print("Illegal move, destination location is occupied.")
            sys.exit()

def check_move(row1, col1, row2, col2):
    

if __name__ == '__main__':
    size = 7
    board = make_board(size)
    print_board(board, size)
    while True:
        peg1 = int(input("Enter the location of the peg to move (RC, -1 to quit):
"))
        row1 = peg1/10
        col1 = peg1%10

        is_valid(row1, col1, True)

        if peg1 == -1:
            print("Player quit.")
            sys.exit()

        peg2 = int(input("Enter the location where the peg is moving to (RC, -1 to quit):"))
        row2 = peg2/10
        col2 = peg2%10

        is_valid(row2, col2, False)

        if peg2 == -1:
            print("Player quit.")
            sys.exit()

    count = 0
    for x in range(size):
        for i in range(size):
            if board[x][i] == "x":
                count += 1
    print("You left %d pegs on board" % count)
