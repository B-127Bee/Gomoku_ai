import random
from copy import deepcopy
import time


class Gomoku:
    def __init__(self):
        self.size = 9
        self.board = [['*' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = 'X'
        self.opponent_player = 'O'
        self.win_length = 5

    def display_board(self):
        """Display the current state of the board."""
        print("   " + " ".join(str(i) for i in range(self.size)))

        # Print each row with its index
        for i, row in enumerate(self.board):
            print(f"{i:2} " + " ".join(row))  # Row index and row content
        print()

    def is_empty(self, x, y):
        """Check if a cell is empty."""
        return self.board[x][y] == '*'

    def make_move(self, x, y, player):
        """Make a move on the board."""
        if self.is_empty(x, y):
            self.board[x][y] = player
            return True
        return False

    def find_threats(self):
        """Find all moves where the opponent is about to win or about to form four in a row."""
        threats = {'my_winning': [], 'opponent_winning': [], 'four': []}
        for x in range(self.size):
            for y in range(self.size):
                if self.is_empty(x, y):
                    # simulate current
                    self.board[x][y] = self.current_player
                    if self.check_winner(player=self.current_player):
                        threats['my_winning'].append((x, y))
                    elif self.check_four_in_a_row(self.board, self.current_player):
                        threats['four'].append((x, y))

                    # simulate opponent
                    self.board[x][y] = self.opponent_player
                    if self.check_winner(player=self.opponent_player):
                        threats['opponent_winning'].append((x, y))

                    # fixed
                    self.board[x][y] = '*'
        return threats

    def check_four_in_a_row(self, board, player):
        """Check if a player has four consecutive pieces and needs one more to win."""
        for x in range(self.size):
            for y in range(self.size):
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (1, -1), (1, 1)]:
                    count = 0
                    for i in range(4):
                        nx, ny = x + i * dx, y + i * dy
                        if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:
                            count += 1
                        else:
                            break
                    if count == 4:  # Found 4 pieces in a row, check if the next move is open
                        nx, ny = x + 4 * dx, y + 4 * dy
                        if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == '*':
                            return True
        return False

    def check_winner(self, board=None, player=None):
        """Check if the given player has won."""
        if board is None:
            board = self.board
        if player is None:
            raise ValueError("Player must be specified.")
        
        for x in range(self.size):
            for y in range(self.size):
                if (self.check_direction(board, x, y, 1, 0, player) or  # Horizontal
                        self.check_direction(board, x, y, 0, 1, player) or  # Vertical
                        self.check_direction(board, x, y, 1, 1, player) or  # Diagonal \
                        self.check_direction(board, x, y, 1, -1, player)):  # Diagonal /
                    return True
        return False

    def check_direction(self, board, x, y, dx, dy, player):
        """Check a specific direction for connected pieces."""
        count = 0
        for i in range(self.win_length):
            nx, ny = x + i * dx, y + i * dy
            if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:
                count += 1
            else:
                break
        return count == self.win_length

    def evaluate_move(self, board, x, y, player):
        """Evaluate the score of placing a piece at (x, y)."""
        if not self.is_empty(x, y):
            return -float('inf')  # Invalid move

        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        score = 0

        for dx, dy in directions:
            connected = 0
            # Count connected pieces in one direction
            for i in range(1, self.win_length):
                nx, ny = x + i * dx, y + i * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:
                    connected += 1
                else:
                    break

            # Count connected pieces in the opposite direction
            for i in range(1, self.win_length):
                nx, ny = x - i * dx, y - i * dy
                if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:
                    connected += 1
                else:
                    break

            # Assign higher score for more connected pieces
            if connected + 1 >= self.win_length:
                return 1000  # Winning move
            score += 10 ** connected

        return score

    def best_move(self, board, player):
        """Find the best move for the given player based on evaluation."""
        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if self.is_empty(x, y)]
        best_score = -float('inf')
        best_move = None

        for x, y in empty_cells:
            score = self.evaluate_move(board, x, y, player)
            # Prioritize blocking opponent's winning moves
            opponent_score = self.evaluate_move(board, x, y, 'O' if player == 'X' else 'X')
            score = max(score, opponent_score)  # Prioritize blocking

            if score > best_score:
                best_score = score
                best_move = (x, y)

        return best_move

    def simulate_game(self, board, current_player):
        """Simulate a random game until a winner is found."""
        current_turn = current_player

        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if board[x][y] == '*']

        while empty_cells:
            # Randomly pick an empty cell
            self.searched_nodes += 1
            x, y = random.choice(empty_cells)
            board[x][y] = current_turn

            # Check for a winner
            if self.check_winner(board=board, player=current_turn):
                return current_turn

            # Switch players
            current_turn = 'O' if current_turn == 'X' else 'X'
            empty_cells.remove((x, y))  # Avoid unnecessary re-calculation

        return None  # If no winner, it's a draw

    def mcts(self, player='X', simulations_per_move=50):
        """Calculate the best move using Monte Carlo Tree Search."""
        opponent = 'O' if player == 'X' else 'X'
        self.searched_nodes = 0
        start_time = time.time()

        # Check for the opponent's threats (five in a row or four in a row)
        threats = self.find_threats()
        if threats['my_winning']:
            return threats['my_winning'][0]  
        if threats['opponent_winning']:
            return threats['opponent_winning'][0] 

        # Perform MCTS for other moves
        # empty_cells = list(self.get_relevant_moves())  # Use relevant moves instead of all empty cells
        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if self.board[x][y] == '*']
        move_scores = {}

        for x, y in empty_cells:
            win_count = 0

            for _ in range(simulations_per_move):
                
                simulated_board = deepcopy(self.board)
                simulated_board[x][y] = player  
                
                if self.simulate_game(simulated_board, opponent) == player:
                    win_count += 1

            move_scores[(x, y)] = win_count / simulations_per_move

        # Handle the case when move_scores is empty
        if not move_scores:
            raise RuntimeError("No valid moves available for the AI.")

        # Select the move with the highest win rate
        best_move = max(move_scores, key=move_scores.get)
        print(f"Best move for player {player} is {best_move} with win rate {move_scores[best_move]:.2f}")
        elapsed_time = time.time() - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Searched nodes: {self.searched_nodes}")
        return best_move
    
    def get_relevant_moves(self):
        """Find moves near existing pieces to reduce the search space."""
        relevant_moves = set()
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        high_priority = []

        for x in range(self.size):
            for y in range(self.size):
                if not self.is_empty(x, y):  # If there's a piece at (x, y)
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.size and 0 <= ny < self.size and self.is_empty(nx, ny):
                            if self.check_four_in_a_row(self.board, self.current_player):
                               high_priority.append((nx, ny))  # record higher priority step
                            relevant_moves.add((nx, ny))

        # Fallback: If no moves are found near pieces, consider all empty cells
        if not relevant_moves:
            relevant_moves = {(x, y) for x in range(self.size) for y in range(self.size) if self.is_empty(x, y)}

        return relevant_moves

    def play(self):
        """Main game loop."""
        while True:
            self.display_board()

            if self.check_winner(player=self.opponent_player):
                print(f"Player {self.opponent_player} wins!")
                break

            if self.current_player == 'O':  # AI's turn
                print("AI is calculating its move...")
                x, y = self.mcts(player=self.current_player)
            else:  # Human or opponent's turn
                try:
                    x, y = map(int, input("Enter your move (row and column): ").split())
                    if not (0 <= x < self.size and 0 <= y < self.size):
                        raise ValueError
                except ValueError:
                    print("Invalid input. Enter row and column numbers within the board size.")
                    continue

            if self.make_move(x, y, self.current_player):
                if self.check_winner(player=self.current_player):
                    self.display_board()
                    print(f"Player {self.current_player} wins!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print("Cell is already occupied. Try again.")


# Start the game

game = Gomoku()
game.play()
