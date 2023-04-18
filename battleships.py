from PIL import Image
from random import randint

hit_board = [[' '] * 7 for x in range(7)]
computer_generated_board = [[' '] * 7 for y in range(7)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
ships = []
trafiony_count = 0

global battle_ships_board
global battle_ships_board_with_pieces

global trafiony
global pudlo
global zatopiony


# def show_board(board):
#     print('  A B C D E F G')
#     row = 1
#     for row_board in board:
#         print("%d|%s|" % (row, '|'.join(row_board)))
#         row += 1


def generate_game_board(row, col):

    if hit_board[row][col] == 'X':
        battle_ships_board_with_pieces.paste(trafiony.resize((50, 50)), piece_position(row, col))
    elif hit_board[row][col] == 'o':
        battle_ships_board_with_pieces.paste(pudlo.resize((50, 50)), piece_position(row, col))
    elif hit_board[row][col] == 'O':
        battle_ships_board_with_pieces.paste(zatopiony.resize((50, 50)), piece_position(row, col))
    battle_ships_board_with_pieces.save('images/ships/Battleship_game_board_with_pieces.png')


def clear_board_computer():
    for row in range(7):
        for col in range(7):
            computer_generated_board[row][col] = ' '


def clear_board_hit():
    for row in range(7):
        for col in range(7):
            hit_board[row][col] = ' '


def piece_position(row, col):
    cell_size = battle_ships_board_with_pieces.width // 8
    x = (col * cell_size + cell_size + 20)
    y = (row * cell_size + cell_size + 20)
    return x, y


def squares_around_ship_empty(row, col, length, orientation, board):
    # 0 = horizontal
    if orientation == 0:
        if row == 0:
            if col == 0:
                if board[row][col + length] == ' ':
                    for x in range(length + 1):
                        if board[row + 1][col + x] != ' ':
                            return False
                    return True
        elif row == 6:
            if col == 0:
                if board[row][col + length] == ' ':
                    for x in range(length + 1):
                        if board[row - 1][col + x] != ' ':
                            return False
                    return True
        else:
            if 0 < row < 6:
                if col == 0:
                    if board[row][col + length] == ' ':
                        for x in range(length + 1):
                            if board[row - 1][col + x] != ' ':
                                return False
                        for x in range(length + 1):
                            if board[row + 1][col + x] != ' ':
                                return False
                        return True
                else:
                    if 0 < col < 6 - length:
                        for x in range(length + 2):
                            if board[row - 1][col - 1 + x] != ' ':
                                return False
                        for x in range(length + 2):
                            if board[row + 1][col - 1 + x] != ' ':
                                return False
                        if board[row][col - 1] != ' ':
                            return False
                        if board[row][col + length] != ' ':
                            return False
                        return True

    # 1 = vertical
    elif orientation == 1:
        if col == 0:
            if row == 0:
                if board[row + length][col] == ' ':
                    for x in range(length + 1):
                        if board[row + x][col + 1] != ' ':
                            return False
                    return True
        elif col == 6:
            if row == 0:
                if board[row + length][col] == ' ':
                    for x in range(length + 1):
                        if board[row + x][col - 1] != ' ':
                            return False
                    return True
        else:
            if 0 < col < 6:
                if row == 0:
                    if board[row + length][col] == ' ':
                        for x in range(length + 1):
                            if board[row + x][col - 1] != ' ':
                                return False
                        for x in range(length + 1):
                            if board[row + x][col + 1] != ' ':
                                return False
                        return True
                else:
                    if 0 < row < 6 - length:
                        for x in range(length + 2):
                            if board[row - 1 + x][col - 1] != ' ':
                                return False
                        for x in range(length + 2):
                            if board[row - 1 + x][col + 1] != ' ':
                                return False
                        if board[row - 1][col] != ' ':
                            return False
                        if board[row + length][col] != ' ':
                            return False
                        return True


def generate_and_place_ship():
    # list having coordinates of ships
    # [row, col, ...]

    # place 3 ships of length 1
    for i in range(3):
        while True:
            row = randint(0, 6)
            col = randint(0, 6)
            if computer_generated_board[row][col] == ' ':
                if squares_around_ship_empty(row, col, 1, 0, computer_generated_board):
                    computer_generated_board[row][col] = 'S'
                    ships.append([row, col])
                    # print(row, col, 1, 0)
                    break

    # place 2 ships of length 2
    for i in range(2):
        while True:
            # random horizontal or vertical
            orientation = randint(0, 1)
            # 0 = horizontal
            if orientation == 0:
                row = randint(0, 6)
                col = randint(0, 5)
                if computer_generated_board[row][col] == ' ':
                    if computer_generated_board[row][col + 1] == ' ':
                        if squares_around_ship_empty(row, col, 2, orientation, computer_generated_board):
                            computer_generated_board[row][col] = 'S'
                            computer_generated_board[row][col + 1] = 'S'
                            ships.append([row, col, row, col + 1])
                            # print(row, col, 2, orientation)
                            break
            # 1 = vertical
            elif orientation == 1:
                row = randint(0, 5)
                col = randint(0, 6)
                if computer_generated_board[row][col] == ' ':
                    if computer_generated_board[row + 1][col] == ' ':
                        if squares_around_ship_empty(row, col, 2, orientation, computer_generated_board):
                            computer_generated_board[row][col] = 'S'
                            computer_generated_board[row + 1][col] = 'S'
                            ships.append([row, col, row + 1, col])
                            # print(row, col, 2, orientation)
                            break

    # place 1 ship of length 3
    while True:
        # random horizontal or vertical
        orientation = randint(0, 1)
        # 0 = horizontal
        if orientation == 0:
            row = randint(0, 6)
            col = randint(0, 4)
            if computer_generated_board[row][col] == ' ':
                if computer_generated_board[row][col + 1] == ' ':
                    if computer_generated_board[row][col + 2] == ' ':
                        if squares_around_ship_empty(row, col, 3, orientation, computer_generated_board):
                            computer_generated_board[row][col] = 'S'
                            computer_generated_board[row][col + 1] = 'S'
                            computer_generated_board[row][col + 2] = 'S'
                            ships.append([row, col, row, col + 1, row, col + 2])
                            # print(row, col, 3, orientation)
                            break
        # 1 = vertical
        elif orientation == 1:
            row = randint(0, 4)
            col = randint(0, 6)
            if computer_generated_board[row][col] == ' ':
                if computer_generated_board[row + 1][col] == ' ':
                    if computer_generated_board[row + 2][col] == ' ':
                        if squares_around_ship_empty(row, col, 3, orientation, computer_generated_board):
                            computer_generated_board[row][col] = 'S'
                            computer_generated_board[row + 1][col] = 'S'
                            computer_generated_board[row + 2][col] = 'S'
                            ships.append([row, col, row + 1, col, row + 2, col])
                            # print(row, col, 3, orientation)
                            break


def get_coordinates_from_user():
    row = input('Podaj rząd 1-7: ')
    while row not in ['1', '2', '3', '4', '5', '6', '7']:
        print('Nieprawidłowy rząd!')
        row = input('Podaj rząd 1-7: ')
    col = input('Podaj kolumnę A-G: ').upper()
    while col not in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        print('Nieprawidłowa kolumna!')
        col = input('Podaj kolumnę A-G: ').upper()

    col = letters_to_numbers[col]
    return int(row) - 1, col


# def count_hit_ships(board):
#     count = 0
#     for row in board:
#         for col in row:
#             if col == 'O':
#                 count += 1
#     return count


# def check_if_game_over():
#     # if count_hit_ships(player_board) == 10:
#     #     print('Przegrałeś!')
#     #     return True
#     if count_hit_ships(computer_generated_board) == 10:
#         # print('Wygrałeś!')
#         # print('Plansza komputera:')
#         show_board(computer_generated_board)
#         return True
#     return False


# def check_if_hit(row, col, board):
#     if board[row][col] == 'S':
#         # board[row][col] = 'X'
#         # hit_board[row][col] = 'X'
#
#         # print('Trafiony!')
#         check_if_sunk(row, col)
#         return True
#     else:
#         # board[row][col] = 'o'
#         # hit_board[row][col] = 'o'
#         # print('Pudło!')
#         return False


def check_if_sunk(row, col):
    for ship in ships:
        if len(ship) == 2:
            if ship[0] == row and ship[1] == col:
                # print('Zatopiony!')
                computer_generated_board[row][col] = 'O'
                hit_board[row][col] = 'O'
                return True
        if len(ship) == 4:
            if ship[0] == row and ship[1] == col:
                if computer_generated_board[ship[2]][ship[3]] == 'X':
                    # print('Zatopiony!')
                    computer_generated_board[ship[0]][ship[1]] = 'O'
                    computer_generated_board[ship[2]][ship[3]] = 'O'
                    hit_board[ship[0]][ship[1]] = 'O'
                    hit_board[ship[2]][ship[3]] = 'O'
                    return True
            elif ship[2] == row and ship[3] == col:
                if computer_generated_board[ship[0]][ship[1]] == 'X':
                    # print('Zatopiony!')
                    computer_generated_board[ship[0]][ship[1]] = 'O'
                    computer_generated_board[ship[2]][ship[3]] = 'O'
                    hit_board[ship[0]][ship[1]] = 'O'
                    hit_board[ship[2]][ship[3]] = 'O'
                    return True
        elif len(ship) == 6:
            if ship[0] == row and ship[1] == col:
                if computer_generated_board[ship[2]][ship[3]] == 'X' and computer_generated_board[ship[4]][ship[5]] == 'X':
                    # print('Zatopiony!')
                    computer_generated_board[ship[0]][ship[1]] = 'O'
                    computer_generated_board[ship[2]][ship[3]] = 'O'
                    computer_generated_board[ship[4]][ship[5]] = 'O'
                    hit_board[ship[0]][ship[1]] = 'O'
                    hit_board[ship[2]][ship[3]] = 'O'
                    hit_board[ship[4]][ship[5]] = 'O'
                    return True
            elif ship[2] == row and ship[3] == col:
                if computer_generated_board[ship[0]][ship[1]] == 'X' and computer_generated_board[ship[4]][ship[5]] == 'X':
                    # print('Zatopiony!')
                    computer_generated_board[ship[0]][ship[1]] = 'O'
                    computer_generated_board[ship[2]][ship[3]] = 'O'
                    computer_generated_board[ship[4]][ship[5]] = 'O'
                    hit_board[ship[0]][ship[1]] = 'O'
                    hit_board[ship[2]][ship[3]] = 'O'
                    hit_board[ship[4]][ship[5]] = 'O'
                    return True
            elif ship[4] == row and ship[5] == col:
                if computer_generated_board[ship[0]][ship[1]] == 'X' and computer_generated_board[ship[2]][ship[3]] == 'X':
                    # print('Zatopiony!')
                    computer_generated_board[ship[0]][ship[1]] = 'O'
                    computer_generated_board[ship[2]][ship[3]] = 'O'
                    computer_generated_board[ship[4]][ship[5]] = 'O'
                    hit_board[ship[0]][ship[1]] = 'O'
                    hit_board[ship[2]][ship[3]] = 'O'
                    hit_board[ship[4]][ship[5]] = 'O'
                    return True
    return False

# def main():
#     generate_and_place_ship()
#     while True:
#         # print('Twoja plansza:')
#         show_board(hit_board)
#         # print('Plansza komputera:')
#         # show_board(computer_generated_board)
#         row, col = get_coordinates_from_user()
#         while computer_generated_board[row][col] == 'X' or computer_generated_board[row][col] == 'o':
#             # print('Już tutaj strzeliłeś!')
#             row, col = get_coordinates_from_user()
#         if check_if_hit(row, col, computer_generated_board):
#             if check_if_game_over():
#                 break
#             # while True:
#             #     row = randint(0, 6)
#             #     col = randint(0, 6)
#             #     if player_board[row][col] == ' ':
#             #         if check_if_hit(row, col, player_board):
#             #             break
#             #         else:
#             #             break
#
#
# if __name__ == '__main__':
#     main()
