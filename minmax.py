
import time
import numpy as np

# initialize board
def initialize_board():
    return np.full((9, 9), "*", dtype=str)

# print board
def print_board(board):
    print("   " + " ".join(str(i) for i in range(9)))
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))

# check valid move
def is_valid_move(board, row, col):
    return 0 <= row < 9 and 0 <= col < 9 and board[row, col] == "*"

# check winner
def check_direction(board, row, col, dr, dc, player):
    count = 0
    for i in range(5):
        r, c = row + i * dr, col + i * dc
        if 0 <= r < 9 and 0 <= c < 9 and board[r, c] == player:
            count += 1
        else:
            break
    return count == 5

def check_winner(board, player):
    for row in range(9):
        for col in range(9):
            if (
                check_direction(board, row, col, 1, 0, player) or
                check_direction(board, row, col, 0, 1, player) or
                check_direction(board, row, col, 1, 1, player) or
                check_direction(board, row, col, 1, -1, player)
            ):
                return True
    return False

# evaluation
def evaluate_board(board):
    score = 0
    for row in range(9):
        for col in range(9):
            if board[row, col] == 'O':  # AI
                score += evaluate_position(board, row, col, 'O')
            elif board[row, col] == 'X':  # Player
                score -= evaluate_position(board, row, col, 'X')  
    return score

def evaluate_position(board, row, col, player):
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for dr, dc in directions:
        line_score = 0
        for step in range(-4, 5):
            r, c = row + dr * step, col + dc * step
            if 0 <= r < 9 and 0 <= c < 9 and board[r, c] == player:
                line_score += 1
            elif 0 <= r < 9 and 0 <= c < 9 and board[r, c] != '*':
                line_score = 0
            if line_score >= 5:
                return float('inf') if player == 'O' else float('-inf')  
        score += line_score
    return score

# generate legal moves
def generate_legal_moves(board):
    moves = set()
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(9):
        for col in range(9):
            if board[row, col] != "*":
                for dr, dc in directions:
                    for dist in range(1, 2):  # Limit to a distance of 1
                        r, c = row + dr * dist, col + dc * dist
                        if 0 <= r < 9 and 0 <= c < 9 and board[r, c] == "*":
                            moves.add((r, c))
    return list(moves)


# minimax algorithm
def minimax(board, depth, maximizing_player):
    if depth == 0 or check_winner(board, "X") or check_winner(board, "O"):
        return evaluate_board(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_legal_moves(board):
            make_move_in_place(board, move, "O")
            eval = minimax(board, depth - 1, False)
            undo_move_in_place(board, move)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in generate_legal_moves(board):
            make_move_in_place(board, move, "X")
            eval = minimax(board, depth - 1, True)
            undo_move_in_place(board, move)
            min_eval = min(min_eval, eval)
        return min_eval

# AI move
def ai_move(board):
    start_time = time.time()
    moves = generate_legal_moves(board)
    best_score = float('-inf')
    best_move = None
    depth = 3  # Fixed depth

    for move in moves:
        make_move_in_place(board, move, "O")
        score = minimax(board, depth, False)
        undo_move_in_place(board, move)
        if score > best_score:
            best_score = score
            best_move = move

    end_time = time.time()
    print(f"AI thinking time: {end_time - start_time:.6f} seconds")
    return best_move

def make_move_in_place(board, move, player):
    board[move] = player

def undo_move_in_place(board, move):
    board[move] = "*"

# main
def minimax_play_game():
    board = initialize_board()
    print("Welcome to Gomoku! You are the player 'X'")
    print_board(board)

    while True:
        while True:
            try:
                row, col = map(int, input("Enter your move (row column): ").split())
                if is_valid_move(board, row, col):
                    board[row, col] = "X"
                    break
                else:
                    print("Invalid drop, please try again!")
            except ValueError:
                print("The format is incorrect, please enter valid rows and columns!")
        
        print_board(board)
        if check_winner(board, "X"):
            print("You Win!")
            break

        print("AI is thinking...")
        move = ai_move(board)
        if move:
            board[move] = "O"
            print(f"AI drop position: {move}")
            print_board(board)
            if check_winner(board, "O"):
                print("Sorry, you lose!")
                break
        else:
            print("Draw!")
            break

if __name__ == "__main__":
    minimax_play_game()
