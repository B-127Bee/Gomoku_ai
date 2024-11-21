# Constants
PLAYER_X = 'X' # user
PLAYER_O = 'O' # agent
EMPTY = '*'
BOARD_SIZE = 9
WINNING_LENGTH = 5

DIRECTION = [[0,  -1, 0, 1],
             [-1, 0,  1, 0],
             [-1, -1, 1, 1],
             [-1, 1,  1, -1]]
DEPTH = 3
MOVE = (0, 0)

LIAN_5 = "11111"
HUO_4 = "011110"
HUO_3_1 = "001110"
HUO_3_2 = HUO_3_1[::-1]
HUO_3_3 = "010110"
HUO_3_4 = HUO_3_3[::-1]
HUO_2_1 = "001100"
HUO_2_2 = "010100"
HUO_2_3 = HUO_2_2[::-1]
CHONG_4_1 = "-11110"
CHONG_4_2 = CHONG_4_1[::-1]
CHONG_4_3 = "10111"
CHONG_4_4 = CHONG_4_3[::-1]
CHONG_4_5 = "11011"
MIAN_3_1 = "00111-"
MIAN_3_2 = MIAN_3_1[::-1]
MIAN_3_3 = "01101-"
MIAN_3_4 = MIAN_3_3[::-1]
MIAN_3_5 = "01011-"
MIAN_3_6 = MIAN_3_5[::-1]
MIAN_3_7 = "10011"
MIAN_3_8 = MIAN_3_7[::-1]
MIAN_3_9 = "10101"
MIAN_3_10 = "-01110-"
MIAN_2_1 = "00011-"
MIAN_2_2 = MIAN_2_1[::-1]
MIAN_2_3 = "00101-"
MIAN_2_4 = MIAN_2_3[::-1]
MIAN_2_5 = "01001-"
MIAN_2_6 = MIAN_2_5[::-1]
MIAN_2_7 = "10001"

# Check current pos is in center
def is_center(board, row, col):
    return 3 <= row < 6 and 3 <= col < 6

# Check if move is valid
def is_valid_move(board, row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY

def is_pos_valid(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

# initialize board
def initialize_board():
    return [["*" for _ in range(9)] for _ in range(9)]

# Check if game is over
def is_game_over(board, last_move, player):
    if last_move is None:
        return False

    row, col = last_move

    for direction in DIRECTION:
        # including the last step
        count = 1

        # checking forward
        r, c = row + direction[2], col + direction[3]
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            if count == WINNING_LENGTH:
                return True
            r, c = r + direction[2], c + direction[3]

        # checking backward
        r, c = row + direction[0], col + direction[1]
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            if count == WINNING_LENGTH:
                return True
            r, c = r + direction[0], c + direction[1]

    return False

# Heuristic evaluation function
def heuristic_evaluation(board):
    self_s = 0
    opponent_s = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == PLAYER_O:
                self_s += val_f(board, (i, j), PLAYER_O)
            elif board[i][j] == PLAYER_X:
                opponent_s += val_f(board,(i, j), PLAYER_X)
    return self_s - opponent_s

# Check current set of chess's pattern to calculate the score
def evaluate_pattern(s):
    score = 0
    if s.find(LIAN_5) != -1:
        score += 100000000
    if s.find(HUO_4) != -1:
        score += 1000000
    if any(s.find(pattern) != -1 for pattern in [CHONG_4_1, CHONG_4_2, CHONG_4_3, CHONG_4_4, CHONG_4_5]):
        score += 80000
    if any(s.find(pattern) != -1 for pattern in [HUO_3_1, HUO_3_2, HUO_3_3, HUO_3_4]):
        score += 50000
    if any(s.find(pattern) != -1 for pattern in [MIAN_3_1, MIAN_3_2, MIAN_3_3, MIAN_3_4, MIAN_3_5, MIAN_3_6, MIAN_3_7, MIAN_3_8, MIAN_3_9, MIAN_3_10]):
        score += 30000
    if any(s.find(pattern) != -1 for pattern in [HUO_2_1, HUO_2_2, HUO_2_3]):
        score += 10000
    if any(s.find(pattern) != -1 for pattern in [MIAN_2_1, MIAN_2_2, MIAN_2_3, MIAN_2_4, MIAN_2_5, MIAN_2_6, MIAN_2_7]):
        score += 5000

    return score

# Check current position and its surrounding chess pattern to calculate the total score
def val_f(board, pos, player):
    x = pos[0]
    y = pos[1]
    score = 0
    weight = 1

    # add additional weight to center
    if is_center(board, pos[0], pos[1]):
        if pos[0] == 4 and pos[1] == 4:
            weight = 1.5
        else:
            weight = 1.25

    for direction in DIRECTION:
        s = ""
        for i in range(-4, 5):  # 检查9个位置，中心是当前位置
            r = x + i * direction[2]
            c = y + i * direction[3]
            if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                if board[r][c] == player:
                    s += '1'
                elif board[r][c] == EMPTY:
                    s += '0'
                else:
                    s += '-'
            else:
                s += '#'

        score += evaluate_pattern(s)

    return score * weight

def max_value(board, depth, alpha, beta, player, last_move):
    if depth == 0 or is_game_over(board, last_move, player):
        return heuristic_evaluation(board), last_move
    v = float('-inf')
    if player == PLAYER_X:
        op_player = PLAYER_O
    else:
        op_player = PLAYER_X
    best_move = None

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = player
                v_tmp, _ = min_value(board, depth - 1, alpha, beta, op_player, (i, j))
                board[i][j] = EMPTY
                if v_tmp > v:
                    v = v_tmp
                    best_move = (i, j)
                alpha = max(alpha, v)
                if alpha >= beta:
                    return v, best_move
    return v, best_move

def min_value(board, depth, alpha, beta, player, last_move):
    if depth == 0 or is_game_over(board, last_move, player):
        return heuristic_evaluation(board), last_move
    v = float('inf')
    if player == PLAYER_X:
        op_player = PLAYER_O
    else:
        op_player = PLAYER_X
    best_move = None

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = player
                v_tmp, _ = max_value(board, depth - 1, alpha, beta, op_player, (i, j))
                board[i][j] = EMPTY
                if v_tmp < v:
                    v = v_tmp
                    best_move = (i, j)
                beta = min(beta, v)
                if alpha >= beta:
                    return v, best_move
    return v, best_move

def alpha_beta(board, last_move):
    alpha = float('-inf')
    beta = float('inf')
    _, move = max_value(board, DEPTH, alpha, beta, PLAYER_O, last_move)
    return move[0], move[1]

def print_board(board):
    print("   " + " ".join(str(i) for i in range(9)))
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))

# Main function to play the game
def play_game():

    global board
    board = initialize_board()
    while True:
        try:
            row, col = map(int, input("输入你的落子位置 (行 列): ").split())
            if is_valid_move(board, row, col):
                board[row][col] = PLAYER_X
                last_move = (row, col)
                print_board(board)
            else:
                print("无效的落子位置，请重试。")
                continue
        except ValueError:
            print("输入无效，请输入两个由空格分隔的数字。")
            continue

        if is_game_over(board, last_move, PLAYER_X):
            print_board(board)
            print("你赢了！")
            break

        print("AI回合")
        ai_row, ai_col = alpha_beta(board, last_move)
        print(ai_row, ai_col)
        board[ai_row][ai_col] = PLAYER_O
        last_move = (ai_row, ai_col)
        print_board(board)

        if is_game_over(board, last_move, PLAYER_O):
            print_board(board)
            print("AI赢了！")
            break

        if all(EMPTY not in row for row in board):
            print_board(board)
            print("平局！")
            break


if __name__ == "__main__":
    play_game()
