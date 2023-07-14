import random


# Introduction to the game
def begin():
    print("Welcome user! Are you excited to play Tic Tac Toe?")
    input("Press any key to continue.")


# Create board
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


# Function for printing the board
def print_board():
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('--------')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('--------')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Defining players
def choose_symbols():
    while True:
        p_one = input("Player 1, choose X or O: ").upper()
        if p_one not in ['X', 'O']:
            print("Invalid key. Choose X or O.")
            continue
        p_two = 'O' if p_one == 'X' else 'X'
        print(f"Player 2, you are {p_two}")
        return (p_one, p_two)


# Check if the board is full
def is_board_full():
    return all(cell != " " for cell in board.values())


# Check if a player has won
def check_winner(board):
    winning_combinations = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],  # rows
        ['7', '4', '1'], ['8', '5', '2'], ['9', '6', '3'],  # columns
        ['7', '5', '3'], ['9', '5', '1']  # diagonals
    ]
    for combination in winning_combinations:
        if board[combination[0]] \
                == board[combination[1]] \
                == board[combination[2]] != " ":
            return True, board[combination[0]]
    return False, ""


# Get the available spots on the board
def get_available_spots():
    return [position for position, value in board.items() if value == " "]


# Player's turn
def player_turn(player_symbol):
    while True:
        position = input(f"Player's ({player_symbol}) turn. \
            Choose a spot (1-9): ")
        if position not in board.keys():
            print("Invalid spot! Choose another spot (1-9).")
            continue
        if board[position] != " ":
            print("Spot already taken! Choose another spot.")
            continue
        return position


# Computer's turn (random move)
def computer_turn(computer_symbol):
    position = random.choice(get_available_spots())
    print(f"Computer's ({computer_symbol}) turn. Choosing spot {position}")
    return position


# Play the game
def play_game():
    begin()
    players = choose_symbols()
    symbols = [players[0], players[1]]
    current_player = 0

    while True:
        print_board()
        player_symbol = symbols[current_player]

        if current_player == 0:
            position = player_turn(player_symbol)
        else:
            position = computer_turn(player_symbol)

        board[position] = player_symbol

        wins, winner = check_winner(board)
        if wins:
            print_board()
            if winner == "draw":
                print("This is a draw!")
            else:
                print(f"{winner} is the winner!")
            break
        elif is_board_full():
            print_board()
            print("The game is a draw!")
            break

        current_player = (current_player + 1) % 2

    play_again = input("Press 'Y' if you would like to \
        play again or any key to exit: ").lower()
    if play_again == "y":
        reset_board()
        play_game()
    else:
        print("Game has ended!")


# Reset the board for a new game
def reset_board():
    global board
    board = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}


# Play the game
play_game()
