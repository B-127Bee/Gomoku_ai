import numpy as np

def create_board():
    return [["*" for _ in range(9)] for _ in range(9)]

def is_terminal_state(board):
    def check_five(line):
        for i in range(len(line) - 4):
            if abs(sum(line[i:i+5])) == 5:
                return True
        return False

    numeric_board = np.array([[1 if cell == "X" else -1 if cell == "O" else 0 for cell in row] for row in board])
    
    for i in range(9):
        if check_five(numeric_board[i, :]) or check_five(numeric_board[:, i]):
            return True

    diags = [numeric_board.diagonal(i) for i in range(-8, 9)]
    anti_diags = [np.fliplr(numeric_board).diagonal(i) for i in range(-8, 9)]
    for diag in diags + anti_diags:
        if len(diag) >= 5 and check_five(diag):
            return True

    if not any("*" in row for row in board):
        return True

    return False

def evaluate(board):
    """
    Improved evaluation function: detect triple patterns and increase defensive weight.
    """
    score = 0
    patterns = {
        (1, 1, 1, 1, 1): 100000,  
        (1, 1, 1, 1, 0): 10000,   
        (1, 1, 1, 0, 0): 500,     
        (-1, -1, -1, -1, -1): -100000,  
        (-1, -1, -1, -1, 0): -10000,  
        (-1, -1, -1, 0, 0): -500,      
    }

    numeric_board = np.array([[1 if cell == "X" else -1 if cell == "O" else 0 for cell in row] for row in board])

    non_empty_positions = np.argwhere(numeric_board != 0)
    for pos in non_empty_positions:
        row, col = pos
        
        lines = [
            numeric_board[row, max(0, col-4):min(9, col+5)],  
            numeric_board[max(0, row-4):min(9, row+5), col],  
            numeric_board.diagonal(col-row),                 
            np.fliplr(numeric_board).diagonal(8-row-col)    
        ]
        for line in lines:
            if len(line) >= 5:  
                for pattern, value in patterns.items():
                    pattern_str = ''.join(map(str, pattern))
                    line_str = ''.join(map(str, line))
                    score += line_str.count(pattern_str) * value

    return score


def get_legal_moves(board):
    moves = set()
    numeric_board = np.array([[1 if cell == "X" else -1 if cell == "O" else 0 for cell in row] for row in board])
    non_empty_positions = np.argwhere(numeric_board != 0)
    for pos in non_empty_positions:
        row, col = pos
        for dr in range(-2, 3):
            for dc in range(-2, 3):
                r, c = row + dr, col + dc
                if 0 <= r < 9 and 0 <= c < 9 and board[r][c] == "*":
                    moves.add((r, c))
    return list(moves)

def minimax(board, depth, alpha, beta, is_maximizing_player):
    if is_terminal_state(board) or depth == 0:
        return evaluate(board), None

    if is_maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_legal_moves(board):
            i, j = move
            board[i][j] = "X"
            eval, _ = minimax(board, depth - 1, alpha, beta, False)
            board[i][j] = "*"
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_legal_moves(board):
            i, j = move
            board[i][j] = "O"
            eval, _ = minimax(board, depth - 1, alpha, beta, True)
            board[i][j] = "*"
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move


def print_board(board):
    print("   " + " ".join(str(i) for i in range(9)))
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))


def play_game():
    board = create_board()
    turn = "O"  
    while not is_terminal_state(board):
        print_board(board)

        if turn == "O": 
            valid_input = False
            while not valid_input:
                try:
                    user_input = input("Please enter your chess position (row and column, e.g. '1 1' or '1,1'):")
                    user_input = user_input.replace('，', ',')
                    if ',' in user_input:
                        row, col = map(int, user_input.split(','))
                    else:
                        row, col = map(int, user_input.split())
                    if board[row][col] == "*":
                        valid_input = True
                    else:
                        print("Invalid location! The location is already occupied.")
                except (ValueError, IndexError):
                    print("Invalid input! Please try again.")
            board[row][col] = "O"
        else:  
            print("AI is thinking...")
            _, ai_move = minimax(board, depth=3, alpha=float('-inf'), beta=float('inf'), is_maximizing_player=True)
            if ai_move:
                board[ai_move[0]][ai_move[1]] = "X"

        turn = "X" if turn == "O" else "O"

    print_board(board)
    print("game over！")
    if is_terminal_state(board):
        print("Congratulations! You won！" if turn == "X" else "Unfortunately, AI wins！")
    else:
        print("draw！")

if __name__ == "__main__":
    play_game()