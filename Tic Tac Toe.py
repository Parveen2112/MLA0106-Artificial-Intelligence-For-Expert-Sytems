import random

# Initialize empty board
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("---------")
    print()

def check_winner(player):
    # All possible winning combinations
    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_conditions)

def is_full():
    return " " not in board

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
            else:
                board[move] = "X"
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")

def ai_move():
    print("AI is making a move...")
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available_moves)
    board[move] = "O"

def main():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        human_move()
        print_board()
        if check_winner("X"):
            print("🎉 You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        ai_move()
        print_board()
        if check_winner("O"):
            print("💻 AI wins!")
            break
        if is_full():
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
