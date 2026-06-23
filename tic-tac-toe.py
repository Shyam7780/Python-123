import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Variables
current_player = "X"
board = [""] * 9
x_score = 0
o_score = 0

# Score Update
def update_score():
    score_label.config(text=f"X: {x_score}    O: {o_score}")

# Check Winner
def check_winner():
    win_patterns = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != "":
            # Highlight winning buttons
            for i in (a, b, c):
                buttons[i].config(bg="lightgreen")
            return board[a]
    if "" not in board:
        return "Draw"
    return None

# Reset Board
def reset_board():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    for btn in buttons:
        btn.config(text="", bg="SystemButtonFace")
    turn_label.config(text="Turn: X")

# Reset Scores
def reset_scores():
    global x_score, o_score
    x_score = 0
    o_score = 0
    update_score()
    reset_board()

# Button Click
def on_click(index):
    global current_player, x_score, o_score
    if board[index] == "":
        board[index] = current_player
        color = "blue" if current_player == "X" else "red"
        buttons[index].config(text=current_player, fg=color)

        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                if winner == "X":
                    x_score += 1
                else:
                    o_score += 1
                update_score()
                messagebox.showinfo("Game Over", f"Player {winner} Wins!")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            turn_label.config(text=f"Turn: {current_player}")

# Title
title_label = tk.Label(root, text="Tic-Tac-Toe", font=("Arial", 20, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Score Label
score_label = tk.Label(root, text="X: 0    O: 0", font=("Arial", 14))
score_label.grid(row=1, column=0, columnspan=3, pady=5)

# Buttons
buttons = []
for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 24, "bold"),
        width=4,
        height=2,
        command=lambda i=i: on_click(i)
    )
    btn.grid(row=(i // 3) + 2, column=i % 3)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), command=reset_board)
restart_btn.grid(row=5, column=0, columnspan=3, sticky="nsew", pady=10)

# Reset Scores Button
reset_scores_btn = tk.Button(root, text="Reset Scores", font=("Arial", 12), command=reset_scores)
reset_scores_btn.grid(row=6, column=0, columnspan=3, sticky="nsew", pady=5)

# Turn Label
turn_label = tk.Label(root, text="Turn: X", font=("Arial", 14))
turn_label.grid(row=7, column=0, columnspan=3, pady=5)

root.mainloop()
