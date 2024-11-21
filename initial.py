# initialize board
def initialize_board():
    return [["*" for _ in range(9)] for _ in range(9)]

# print board
def print_board(board):
    print("   " + " ".join(str(i) for i in range(9)))
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))