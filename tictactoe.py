# tic-tac-toe with AI using minimax algorithm
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 'X'
computer = 'O'
# win = 0
# draw = 0
# loss = 0

# loading images
# tictactoe_board = Image.open('images/tictactoe_board.png')
# tictactoe_board.save('images/tictactoe_board_with_piece.png')
# tictactoe_board.close()
# tictactoe_board_with_piece = Image.open('images/tictactoe_board_with_piece.png')
#
# # circle1 = Image.open('images/circle1.png')
# cross1 = Image.open('images/cross1.png')
# circle2 = Image.open('images/circle2.png')
# # cross2 = Image.open('images/cross2.png')
# # line = Image.open('images/line.png')

global tictactoe_board
global tictactoe_board_with_piece
# global circle1
global cross1
global circle2
# global cross2
# global line


# # function to print the board in one message in discord chat
# def print_board_discord():
#     return f'      *0*    *1*    *2*\n' \
#            f'*0*   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}\n' \
#            f'     ----------\n' \
#            f'*1*    {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}\n' \
#            f'     ----------\n' \
#            f'*2*   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}\n'


def generate_board(row, col):
    cell_size = tictactoe_board.width // 3
    piece_size = cell_size - 100
    if board[row][col] == 'X':
        tictactoe_board_with_piece.paste(cross1.resize((piece_size, piece_size)), piece_position(row, col))
    elif board[row][col] == 'O':
        tictactoe_board_with_piece.paste(circle2.resize((piece_size, piece_size)), piece_position(row, col))
    tictactoe_board_with_piece.save('images/tictactoe_board_with_piece.png')


def piece_position(row, col):
    cell_size = tictactoe_board.width // 3
    piece_size = cell_size - 100
    x = (col * cell_size + (cell_size - piece_size) // 2) - 25
    y = (row * cell_size + (cell_size - piece_size) // 2)
    return x, y


# function to check if the game is won
def check_win(board, player):
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


# # function to return row and col when the game is won
# def win_position(board, player):
#     # check rows
#     for row in range(3):
#         if board[row][0] == board[row][1] == board[row][2] == player:
#             return row, 0, row, 2
#     # check columns
#     for col in range(3):
#         if board[0][col] == board[1][col] == board[2][col] == player:
#             return 0, col, 2, col
#     # check diagonals
#     if board[0][0] == board[1][1] == board[2][2] == player:
#         return 0, 0, 2, 2
#     if board[0][2] == board[1][1] == board[2][0] == player:
#         return 0, 2, 2, 0


# # function taking win position and drawing line on the board
# def draw_line(row1, col1, row2, col2):
#     if row1 == row2:
#         tictactoe_board_with_piece.paste(line.rotate(90), (500, row1 * 150 + 150))
#     elif col1 == col2:
#         tictactoe_board_with_piece.paste(line, (col1 * 150 + 150, 500))
#     elif row1 == col1 and row2 == col2:
#         tictactoe_board_with_piece.paste(line.rotate(45), (500, 500))
#     elif row1 == 2 - col1 and row2 == 2 - col2:
#         tictactoe_board_with_piece.paste(line.rotate(-45), (500, 500))
#     tictactoe_board_with_piece.save('images/tictactoe_board_with_piece.png')


# function minimax is based on pseudocode from wikipedia page of minimax algorithm (
# https://en.wikipedia.org/wiki/Minimax)
def minimax(board, depth, is_max):
    if check_win(board, computer):
        return 10 - depth
    if check_win(board, player):
        return depth - 10
    if not any(' ' in row for row in board):
        return 0

    if is_max:
        best_score = -1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = computer
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score


# returns (row, col) of best move for computer
def best_move(board):
    best_score = -1000
    best_move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = computer
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move


def clear_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
