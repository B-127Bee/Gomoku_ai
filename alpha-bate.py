import time
import initial

# check valid move
def is_valid_move(board, row, col):
    return 0 <= row < 9 and 0 <= col < 9 and board[row][col] == "*"

# caheck winner
def check_direction(board, row, col, dr, dc, player):
    count = 0
    for i in range(5):
        r, c = row + i * dr, col + i * dc
        if 0 <= r < 9 and 0 <= c < 9 and board[r][c] == player:
            count += 1
        else:
            break
    return count == 5

def check_winner(board, player):
    for row in range(9):
        for col in range(9):
            if (
                check_direction(board, row, col, 1, 0, player) or  # horizontal
                check_direction(board, row, col, 0, 1, player) or  # longitudinal
                check_direction(board, row, col, 1, 1, player) or  # diagonal \
                check_direction(board, row, col, 1, -1, player)    # diagonal /
            ):
                return True
    return False


# evaluation
def evaluate_board(board):
    score = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 'O':  # AI
                score += evaluate_position(board, row, col, 'O')
            elif board[row][col] == 'X':  # Player
                score -= evaluate_position(board, row, col, 'X')  
    return score

def evaluate_position(board, row, col, player):
    score = 0
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # 4 directions ,horizontal,longitudinal,diagonal
    for dr, dc in directions:
        line_score = 0
        for step in range(-4, 5):  # Check up to 5 consecutive positions
            r, c = row + dr * step, col + dc * step
            if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == player:
                line_score += 1  # Bonus points when encountering its own pieces
            elif 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] != '*':
                line_score = 0  # Resets when encountering opponent's pieces
            if line_score >= 5: # win
                return float('inf') if player == 'O' else float('-inf')  
        score += line_score
    return score


# Generate all legal drop positions
def generate_legal_moves(board):
    moves = []
    for row in range(9):
        for col in range(9):
            if board[row][col] == "*":
                moves.append((row, col))
    return moves

# Drop on the board
def make_move(board, move, player):
    new_board = [row[:] for row in board]
    row, col = move
    new_board[row][col] = player
    return new_board

# α-β pruning
def alpha_beta_pruning(board, depth, maximizing_player, alpha, beta):
    if depth == 0 or check_winner(board, "X") or check_winner(board, "O"):
        return evaluate_board(board)

    # AI（MAX)
    if maximizing_player:
        max_eval = float('-inf')
        for move in generate_legal_moves(board):
            new_board = make_move(board, move, "O")
            eval = alpha_beta_pruning(new_board, depth - 1, False, alpha, beta)
            max_eval = max(max_eval, eval) # Update 'max_eval' to the maximum value of the current evaluation value
            alpha = max(alpha, eval) # Update 'alpha' to the current maximum
            if beta <= alpha:
                break  # If beta <=alpha, pruning and stop further evaluation
        return max_eval
    
    # player(MIN)
    else:
        min_eval = float('inf')
        for move in generate_legal_moves(board):
            new_board = make_move(board, move, "X")
            eval = alpha_beta_pruning(new_board, depth - 1, True, alpha, beta)
            min_eval = min(min_eval, eval) # Update 'mamin_evalx_eval' to the minimum value of the current evaluation value
            beta = min(beta, eval) # Update 'beta' to the current minimum
            if beta <= alpha:
                break  # If beta <=alpha, pruning and stop further evaluation
        return min_eval

# AI move
def ai_move(board):
    start_time = time.time()  # record start time

    # Prioritize preventing player "X" from winning
    for row in range(len(board)):
        for col in range(len(board[row])):
            if is_valid_move(board, row, col):
                board[row][col] = 'X'  # Simulate player 
                if check_winner(board, 'X'):  # Check if player wins
                    board[row][col] = 'O'  # Prevent player from winning
                    end_time = time.time()  # record ending time
                    print(f"Thinking time: {end_time - start_time:.6f} seconds")
                    return (row, col)
                board[row][col] = '*'  # Undo the simulation
   
    
    # If there is no threat, conduct a routine assessment
    best_score = float('-inf')
    best_move = None
    for row in range(len(board)):
        for col in range(len(board[row])):
            if is_valid_move(board, row, col):
                board[row][col] = 'O'  # Simulate AI
                score = evaluate_board(board)
                board[row][col] = '*'  # Undo the simulation
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    end_time = time.time()  # record ending time
    print(f"Thinking time: {end_time - start_time:.6f} seconds")
    return best_move if best_move else (0, 0)  


# main
def alpha_beta_play_game():
    board = initial.initialize_board()
    print("Welcome to Gomoku! You are the player 'X'")
    initial.print_board(board)

    while True:
        # player
        while True:
            try:
                row, col = map(int, input("Please enter your drop position (format: row column)：").split())
                if is_valid_move(board, row, col):
                    board[row][col] = "X"
                    break
                else:
                    print("Invalid drop, please try again!")
            except ValueError:
                print("The format is incorrect, please enter valid rows and columns!")
        
        initial.print_board(board)
        if check_winner(board, "X"):
            print("You Win!")
            break

        # AI 
        print("AI is thinking...")
        move = ai_move(board)
        if move:
            board[move[0]][move[1]] = "O"
            print(f"AI drop position: {move}")
            initial.print_board(board)
            if check_winner(board, "O"):
                print("Sorry, you lose!")
                break
        else:
            print("Draw!")
            break

if __name__ == "__main__":
    alpha_beta_play_game()
