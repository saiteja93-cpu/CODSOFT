import random

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---|---|---")
    print()

def check_winner(player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        if all(board[pos] == player for pos in condition):
            return True
    return False

def is_board_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move. Try again.")

        except ValueError:
            print("Please enter a number.")

def ai_move():
    available_moves = [i for i in range(9) if board[i] == " "]
    move = random.choice(available_moves)
    board[move] = "O"

print("=== TIC TAC TOE AI ===")
print("You = X | AI = O")

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_board_full():
        print_board()
        print("Match Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_board_full():
        print_board()
        print("Match Draw!")
        break
