{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "10f53097-6960-4cdf-8b04-98fe623411dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   0 1 2 3 4 5 6 7 8\n",
      " 0 * * * * * * * * *\n",
      " 1 * * * * * * * * *\n",
      " 2 * * * * * * * * *\n",
      " 3 * * * * * * * * *\n",
      " 4 * * * * * * * * *\n",
      " 5 * * * * * * * * *\n",
      " 6 * * * * * * * * *\n",
      " 7 * * * * * * * * *\n",
      " 8 * * * * * * * * *\n",
      "\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[87], line 275\u001b[0m\n\u001b[0;32m    272\u001b[0m \u001b[38;5;66;03m# Start the game\u001b[39;00m\n\u001b[0;32m    274\u001b[0m game \u001b[38;5;241m=\u001b[39m Gomoku()\n\u001b[1;32m--> 275\u001b[0m game\u001b[38;5;241m.\u001b[39mplay()\n",
      "Cell \u001b[1;32mIn[87], line 255\u001b[0m, in \u001b[0;36mGomoku.play\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    253\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:  \u001b[38;5;66;03m# Human or opponent's turn\u001b[39;00m\n\u001b[0;32m    254\u001b[0m     \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 255\u001b[0m         x, y \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mmap\u001b[39m(\u001b[38;5;28mint\u001b[39m, \u001b[38;5;28minput\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mEnter your move (row and column): \u001b[39m\u001b[38;5;124m\"\u001b[39m)\u001b[38;5;241m.\u001b[39msplit())\n\u001b[0;32m    256\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m (\u001b[38;5;241m0\u001b[39m \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m x \u001b[38;5;241m<\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msize \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;241m0\u001b[39m \u001b[38;5;241m<\u001b[39m\u001b[38;5;241m=\u001b[39m y \u001b[38;5;241m<\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msize):\n\u001b[0;32m    257\u001b[0m             \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1262\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1260\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1261\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1262\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_input_request(\n\u001b[0;32m   1263\u001b[0m     \u001b[38;5;28mstr\u001b[39m(prompt),\n\u001b[0;32m   1264\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parent_ident[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m   1265\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_parent(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1266\u001b[0m     password\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[0;32m   1267\u001b[0m )\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1305\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1302\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1303\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1304\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1305\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1306\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1307\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "import random\n",
    "from copy import deepcopy\n",
    "import time\n",
    "\n",
    "class Gomoku:\n",
    "    def __init__(self):\n",
    "        self.size = 9\n",
    "        self.board = [['*' for _ in range(self.size)] for _ in range(self.size)]\n",
    "        self.current_player = 'X'\n",
    "        self.opponent_player = 'O'\n",
    "        self.win_length = 5\n",
    "\n",
    "    def display_board(self):\n",
    "        \"\"\"Display the current state of the board.\"\"\"\n",
    "        print(\"   \" + \" \".join(str(i) for i in range(self.size)))\n",
    "\n",
    "        # Print each row with its index\n",
    "        for i, row in enumerate(self.board):\n",
    "            print(f\"{i:2} \" + \" \".join(row))  # Row index and row content\n",
    "        print()\n",
    "\n",
    "    def is_empty(self, x, y):\n",
    "        \"\"\"Check if a cell is empty.\"\"\"\n",
    "        return self.board[x][y] == '*'\n",
    "\n",
    "    def make_move(self, x, y, player):\n",
    "        \"\"\"Make a move on the board.\"\"\"\n",
    "        if self.is_empty(x, y):\n",
    "            self.board[x][y] = player\n",
    "            return True\n",
    "        return False\n",
    "\n",
    "    def find_threats(self):\n",
    "        \"\"\"Find all moves where the opponent is about to win or about to form four in a row.\"\"\"\n",
    "        threats = {'my_winning': [], 'opponent_winning': [], 'four': []}\n",
    "        for x in range(self.size):\n",
    "            for y in range(self.size):\n",
    "                if self.is_empty(x, y):\n",
    "                    # simulate current\n",
    "                    self.board[x][y] = self.current_player\n",
    "                    if self.check_winner(player=self.current_player):\n",
    "                        threats['my_winning'].append((x, y))\n",
    "                    elif self.check_four_in_a_row(self.board, self.current_player):\n",
    "                        threats['four'].append((x, y))\n",
    "\n",
    "                    # simulate opponent\n",
    "                    self.board[x][y] = self.opponent_player\n",
    "                    if self.check_winner(player=self.opponent_player):\n",
    "                        threats['opponent_winning'].append((x, y))\n",
    "\n",
    "                    # fixed\n",
    "                    self.board[x][y] = '*'\n",
    "        return threats\n",
    "\n",
    "    def check_four_in_a_row(self, board, player):\n",
    "        \"\"\"Check if a player has four consecutive pieces and needs one more to win.\"\"\"\n",
    "        for x in range(self.size):\n",
    "            for y in range(self.size):\n",
    "                for dx, dy in [(-1, 0), (0, -1), (1, 0), (1, -1), (1, 1)]:\n",
    "                    count = 0\n",
    "                    for i in range(4):\n",
    "                        nx, ny = x + i * dx, y + i * dy\n",
    "                        if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:\n",
    "                            count += 1\n",
    "                        else:\n",
    "                            break\n",
    "                    if count == 4:  # Found 4 pieces in a row, check if the next move is open\n",
    "                        nx, ny = x + 4 * dx, y + 4 * dy\n",
    "                        if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == '*':\n",
    "                            return True\n",
    "        return False\n",
    "\n",
    "    def check_winner(self, board=None, player=None):\n",
    "        \"\"\"Check if the given player has won.\"\"\"\n",
    "        if board is None:\n",
    "            board = self.board\n",
    "        if player is None:\n",
    "            raise ValueError(\"Player must be specified.\")\n",
    "        \n",
    "        for x in range(self.size):\n",
    "            for y in range(self.size):\n",
    "                if (self.check_direction(board, x, y, 1, 0, player) or  # Horizontal\n",
    "                        self.check_direction(board, x, y, 0, 1, player) or  # Vertical\n",
    "                        self.check_direction(board, x, y, 1, 1, player) or  # Diagonal \\\n",
    "                        self.check_direction(board, x, y, 1, -1, player)):  # Diagonal /\n",
    "                    return True\n",
    "        return False\n",
    "\n",
    "    def check_direction(self, board, x, y, dx, dy, player):\n",
    "        \"\"\"Check a specific direction for connected pieces.\"\"\"\n",
    "        count = 0\n",
    "        for i in range(self.win_length):\n",
    "            nx, ny = x + i * dx, y + i * dy\n",
    "            if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:\n",
    "                count += 1\n",
    "            else:\n",
    "                break\n",
    "        return count == self.win_length\n",
    "\n",
    "    def evaluate_move(self, board, x, y, player):\n",
    "        \"\"\"Evaluate the score of placing a piece at (x, y).\"\"\"\n",
    "        if not self.is_empty(x, y):\n",
    "            return -float('inf')  # Invalid move\n",
    "\n",
    "        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]\n",
    "        score = 0\n",
    "\n",
    "        for dx, dy in directions:\n",
    "            connected = 0\n",
    "            # Count connected pieces in one direction\n",
    "            for i in range(1, self.win_length):\n",
    "                nx, ny = x + i * dx, y + i * dy\n",
    "                if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:\n",
    "                    connected += 1\n",
    "                else:\n",
    "                    break\n",
    "\n",
    "            # Count connected pieces in the opposite direction\n",
    "            for i in range(1, self.win_length):\n",
    "                nx, ny = x - i * dx, y - i * dy\n",
    "                if 0 <= nx < self.size and 0 <= ny < self.size and board[nx][ny] == player:\n",
    "                    connected += 1\n",
    "                else:\n",
    "                    break\n",
    "\n",
    "            # Assign higher score for more connected pieces\n",
    "            if connected + 1 >= self.win_length:\n",
    "                return 1000  # Winning move\n",
    "            score += 10 ** connected\n",
    "\n",
    "        return score\n",
    "\n",
    "    def best_move(self, board, player):\n",
    "        \"\"\"Find the best move for the given player based on evaluation.\"\"\"\n",
    "        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if self.is_empty(x, y)]\n",
    "        best_score = -float('inf')\n",
    "        best_move = None\n",
    "\n",
    "        for x, y in empty_cells:\n",
    "            score = self.evaluate_move(board, x, y, player)\n",
    "            # Prioritize blocking opponent's winning moves\n",
    "            opponent_score = self.evaluate_move(board, x, y, 'O' if player == 'X' else 'X')\n",
    "            score = max(score, opponent_score)  # Prioritize blocking\n",
    "\n",
    "            if score > best_score:\n",
    "                best_score = score\n",
    "                best_move = (x, y)\n",
    "\n",
    "        return best_move\n",
    "\n",
    "    def simulate_game(self, board, current_player):\n",
    "        \"\"\"Simulate a random game until a winner is found.\"\"\"\n",
    "        players = ['X', 'O']\n",
    "        current_turn = current_player\n",
    "\n",
    "        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if board[x][y] == '*']\n",
    "\n",
    "        while empty_cells:\n",
    "            # Randomly pick an empty cell\n",
    "            self.searched_nodes += 1\n",
    "            x, y = random.choice(empty_cells)\n",
    "            board[x][y] = current_turn\n",
    "\n",
    "            # Check for a winner\n",
    "            if self.check_winner(board=board, player=current_turn):\n",
    "                return current_turn\n",
    "\n",
    "            # Switch players\n",
    "            current_turn = 'O' if current_turn == 'X' else 'X'\n",
    "            empty_cells.remove((x, y))  # Avoid unnecessary re-calculation\n",
    "\n",
    "        return None  # If no winner, it's a draw\n",
    "\n",
    "    def mcts(self, player='X', simulations_per_move=50):\n",
    "        \"\"\"Calculate the best move using Monte Carlo Tree Search.\"\"\"\n",
    "        opponent = 'O' if player == 'X' else 'X'\n",
    "        self.searched_nodes = 0\n",
    "        start_time = time.time()\n",
    "\n",
    "        # Check for the opponent's threats (five in a row or four in a row)\n",
    "        threats = self.find_threats()\n",
    "        if threats['my_winning']:\n",
    "            return threats['my_winning'][0]  \n",
    "        if threats['opponent_winning']:\n",
    "            return threats['opponent_winning'][0] \n",
    "\n",
    "        # Perform MCTS for other moves\n",
    "        #empty_cells = list(self.get_relevant_moves())  # Use relevant moves instead of all empty cells\n",
    "        empty_cells = [(x, y) for x in range(self.size) for y in range(self.size) if self.board[x][y] == '*']\n",
    "        move_scores = {}\n",
    "\n",
    "        for x, y in empty_cells:\n",
    "            win_count = 0\n",
    "\n",
    "            for _ in range(simulations_per_move):\n",
    "                \n",
    "                simulated_board = deepcopy(self.board)\n",
    "                simulated_board[x][y] = player  \n",
    "                \n",
    "                if self.simulate_game(simulated_board, opponent) == player:\n",
    "                    win_count += 1\n",
    "\n",
    "\n",
    "            move_scores[(x, y)] = win_count / simulations_per_move\n",
    "\n",
    "        # Handle the case when move_scores is empty\n",
    "        if not move_scores:\n",
    "            raise RuntimeError(\"No valid moves available for the AI.\")\n",
    "\n",
    "        # Select the move with the highest win rate\n",
    "        best_move = max(move_scores, key=move_scores.get)\n",
    "        print(f\"Best move for player {player} is {best_move} with win rate {move_scores[best_move]:.2f}\")\n",
    "        elapsed_time = time.time() - start_time\n",
    "        print(f\"Elapsed time: {elapsed_time:.2f} seconds\")\n",
    "        print(f\"Searched nodes: {self.searched_nodes}\")\n",
    "        return best_move\n",
    "    \n",
    "    def get_relevant_moves(self):\n",
    "        \"\"\"Find moves near existing pieces to reduce the search space.\"\"\"\n",
    "        relevant_moves = set()\n",
    "        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]\n",
    "\n",
    "        for x in range(self.size):\n",
    "            for y in range(self.size):\n",
    "                if not self.is_empty(x, y):  # If there's a piece at (x, y)\n",
    "                    for dx, dy in directions:\n",
    "                        nx, ny = x + dx, y + dy\n",
    "                        if 0 <= nx < self.size and 0 <= ny < self.size and self.is_empty(nx, ny):\n",
    "                            if self.check_four_in_a_row(self.board, self.current_player):\n",
    "                               high_priority.append((nx, ny))  # record higher priority step\n",
    "                            relevant_moves.add((nx, ny))\n",
    "\n",
    "        # Fallback: If no moves are found near pieces, consider all empty cells\n",
    "        if not relevant_moves:\n",
    "            relevant_moves = {(x, y) for x in range(self.size) for y in range(self.size) if self.is_empty(x, y)}\n",
    "\n",
    "        return relevant_moves\n",
    "\n",
    "\n",
    "\n",
    "    def play(self):\n",
    "        \"\"\"Main game loop.\"\"\"\n",
    "        while True:\n",
    "            self.display_board()\n",
    "\n",
    "            if self.check_winner(player=self.opponent_player):\n",
    "                print(f\"Player {self.opponent_player} wins!\")\n",
    "                break\n",
    "\n",
    "            if self.current_player == 'O':  # AI's turn\n",
    "                print(\"AI is calculating its move...\")\n",
    "                x, y = self.mcts(player=self.current_player)\n",
    "            else:  # Human or opponent's turn\n",
    "                try:\n",
    "                    x, y = map(int, input(\"Enter your move (row and column): \").split())\n",
    "                    if not (0 <= x < self.size and 0 <= y < self.size):\n",
    "                        raise ValueError\n",
    "                except ValueError:\n",
    "                    print(\"Invalid input. Enter row and column numbers within the board size.\")\n",
    "                    continue\n",
    "\n",
    "            if self.make_move(x, y, self.current_player):\n",
    "                if self.check_winner(player=self.current_player):\n",
    "                    self.display_board()\n",
    "                    print(f\"Player {self.current_player} wins!\")\n",
    "                    break\n",
    "                self.current_player = 'O' if self.current_player == 'X' else 'X'\n",
    "            else:\n",
    "                print(\"Cell is already occupied. Try again.\")\n",
    "\n",
    "\n",
    "# Start the game\n",
    "\n",
    "game = Gomoku()\n",
    "game.play()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51bd9739-d793-4d1d-8ae7-44f476e439bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "126b9d3a-26ff-470a-ac98-a45fbcd381c1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}