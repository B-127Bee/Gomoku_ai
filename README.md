# Gomoku_ai
Gomoku, also known as "Five in a Row," is a classic two-player strategy game played on a 9×9 grid. Players take turns marking empty spaces with their respective symbols (e.g., "X" and "O"). The objective of the game is to align five of their symbols in a row, either horizontally, vertically, or diagonally, before the opponent does.
The goal of this project is to develop an intelligent Gomoku agent capable of competing against a human player. By leveraging adversarial search algorithms, the agent can make strategic decisions to maximize its chances of winning.
To achieve this, the project implements the following key functionalities:
Game Formulation: Creating the foundational game logic, ensuring smooth human-agent interaction through the terminal.
Minimax Algorithm: Utilizing the minimax algorithm to simulate decision-making processes, allowing the agent to predict optimal moves.
Alpha-Beta Pruning: Enhancing the minimax algorithm by integrating alpha-beta pruning to improve computational efficiency by reducing the search space.
Heuristic Evaluation: Designing a heuristic evaluation function to guide decision-making in limited-depth searches, with emphasis on identifying crucial game patterns such as triples and defensive strategies.
Monte Carlo Tree Search (MCTS): Implementing MCTS to explore probabilistic decision-making, broadening the agent's ability to handle complex scenarios effectively.
This combination of methods ensures the agent demonstrates both strategic foresight and computational efficiency, making it a challenging opponent for human players.
