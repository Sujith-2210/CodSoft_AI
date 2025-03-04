import math

# The game board
board = [' ' for _ in range(9)]

# Function to insert a letter (X or O) at a given position on the board
def insert_letter(letter, pos):
    board[pos] = letter

# Function to check if the space is free
def space_is_free(pos):
    return board[pos] == ' '

# Function to print the board
def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# Function to check if the board is full
def is_board_full(board):
    return board.count(' ') == 0

# Function to check for a win
def is_winner(bo, le):
    return ((bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[0] == le and bo[3] == le and bo[6] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[0] == le and bo[4] == le and bo[8] == le) or
            (bo[2] == le and bo[4] == le and bo[6] == le))

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -10
    elif is_winner(board, 'O'):
        return 10
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if space_is_free(i):
                insert_letter('O', i)
                score = minimax(board, depth + 1, False)
                insert_letter(' ', i)
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if space_is_free(i):
                insert_letter('X', i)
                score = minimax(board, depth + 1, True)
                insert_letter(' ', i)
                best_score = min(score, best_score)
        return best_score

# AI agent's move
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if space_is_free(i):
            insert_letter('O', i)
            score = minimax(board, 0, False)
            insert_letter(' ', i)
            if score > best_score:
                best_score = score
                best_move = i
    insert_letter('O', best_move)
    return

# Human player's move
def human_move():
    pos = int(input('Enter your move (1-9): '))
    insert_letter('X', pos - 1)
    return

# Main game loop
while not(is_board_full(board)):
    print_board(board)
    human_move()
    if is_winner(board, 'X'):
        print_board(board)
        print('Human wins!')
        break
    ai_move()
    if is_winner(board, 'O'):
        print_board(board)
        print('AI wins!')
        break