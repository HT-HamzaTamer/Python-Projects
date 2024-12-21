import tkinter as tk
from tkinter import font
import random


# player turn
def player_turn(row, col):
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "x"
        buttons[row][col]["state"] = "disabled"
    if not check_rows() and not check_cols() and not check_diagonals():
        if check_for_tie():
            return
        computer_turn()

def computer_turn():
    empty_buttons = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]
    if empty_buttons:
        row, col = random.choice(empty_buttons)
        buttons[row][col]["text"] = "o"
        buttons[row][col]["state"] = "disabled"
    if not check_rows() and not check_cols() and not check_diagonals():
        if check_for_tie():
            return

def restart():
    for row in buttons:
        for button in row:
            button["text"] = ""
            button["state"] = "normal"
            wl_label["text"] = ""
            tie_label["text"] = ""
            button.config(bg="SystemButtonFace", fg="black")

def disable_buttons():
    for row in buttons:
        for button in row:
            button["state"] = "disabled"

def update_score(label):
    try:
        current_score = int(label["text"])
        label["text"] = str(current_score + 1)
    except ValueError:
        label["text"] = "1"

def check_rows():
    for row in buttons:
        if all(button["text"] == "x" for button in row):
            wl_label["text"] = "x wins !"

            update_score(my_score_var)
            for button in row:
                button.config(bg="#00CFF0", fg="white")
            disable_buttons()
            return True
        elif all(button["text"] == "o" for button in row):
            wl_label["text"] = "o wins !"

            update_score(computer_score_var)
            for button in row:
                button.config(bg="red", fg="white")
            disable_buttons()
            return True
    return False

def check_cols():
    for col in range(3):
        if all(buttons[row][col]["text"] == "x" for row in range(3)):
            wl_label["text"] = "x wins !"

            update_score(my_score_var)
            for row in range(3):
                buttons[row][col].config(bg="#00CFF0", fg="white")
            disable_buttons()
            return True
        elif all(buttons[row][col]["text"] == "o" for row in range(3)):
            wl_label["text"] = "o wins !"

            update_score(computer_score_var)
            for row in range(3):
                buttons[row][col].config(bg="red", fg="white")
            disable_buttons()
            return True
    return False

def check_diagonals():
    if all(buttons[i][i]["text"] == "x" for i in range(3)):
        wl_label["text"] = "x wins !"
        update_score(my_score_var)
        for i in range(3):
            buttons[i][i].config(bg="#00CFF0", fg="white")
        disable_buttons()
        return True
    elif all(buttons[i][i]["text"] == "o" for i in range(3)):
        wl_label["text"] = "o wins !"
        update_score(computer_score_var)
        for i in range(3):
            buttons[i][i].config(bg="red", fg="white")
        disable_buttons()
        return True

    elif all(buttons[i][2 - i]["text"] == "x" for i in range(3)):
        wl_label["text"] = "x wins !"
        update_score(my_score_var)
        for i in range(3):
            buttons[i][2 - i].config(bg="#00CFF0", fg="white")
        disable_buttons()
        return True
    elif all(buttons[i][2 - i]["text"] == "o" for i in range(3)):
        wl_label["text"] = "o wins !"
        update_score(computer_score_var)
        for i in range(3):
            buttons[i][2 - i].config(bg="red", fg="white")
        disable_buttons()
        return True

    return False

def check_for_tie():
    if all(button["state"] == "disabled" for row in buttons for button in row) and not check_rows() and not check_cols() and not check_diagonals():
        tie_label["text"] = "Tie, no winner"
        for row in buttons:
            for button in row:
                button.config(bg="red", fg="white")


# window
window = tk.Tk()
window.title("Tic Tac Toe")
window.maxsize(width=438, height=557)
window.minsize(width=438, height=557)

# frames
row_frame0 = tk.Frame(window)
row_frame0.place(x=100, y=30)

wlt_frame = tk.Frame(window)
wlt_frame.place(x=100, y=80)

restart_frame = tk.Frame(window)
restart_frame.place(x=180, y=140)

playground_frame = tk.Frame(window)
playground_frame.place(x=0, y=190)

# score
my_score = tk.Label(row_frame0, text="You : ", font=("", 19, ""))
my_score.grid(column=0, row=0)

my_score_var = tk.Label(row_frame0, text="0", font=("", 19, ""))
my_score_var.grid(column=1, row=0)

computer_score = tk.Label(row_frame0, text="Computer : ", font=("", 19, ""))
computer_score.grid(column=2, row=0, padx=(20, 0))

computer_score_var = tk.Label(row_frame0, text="0", font=("", 19, ""))
computer_score_var.grid(column=3, row=0)

# Win, lose and Tie label.
tie_label = tk.Label(wlt_frame, text="", font=("", 33, ""))
tie_label.grid(column=1, row=1)

wl_label = tk.Label(wlt_frame, text="", font=("", 33, ""))
wl_label.grid(column=2, row=1, padx=(50, 0))

# restart button
restart_button = tk.Button(restart_frame, text="Restart", font=("", 15, ""), command=restart)
restart_button.grid(column=1, row=2)

# the game
button_font = font.Font(size=30)
buttons = []
for row in range(3):
    row_buttons = []
    for col in range(3):
        cell = tk.Button(
            playground_frame,
            borderwidth=1,
            width=6,
            height=2,
            text="",
            font=button_font,
            anchor="center",
            command=lambda r=row, c=col: player_turn(r, c)
        )
        row_buttons.append(cell)
        cell.grid(row=row, column=col)
    buttons.append(row_buttons)

window.mainloop()
