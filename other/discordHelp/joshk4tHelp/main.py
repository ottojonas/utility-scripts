import dearpygui.dearpygui as dpg

# Initialize game state
board = [["" for _ in range(3)] for _ in range(3)]
currentPlayer = "X"


def checkWin():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if (
        board[0][0] == board[1][1] == board[2][2] != ""
        or board[0][2] == board[1][1] == board[2][0] != ""
    ):
        return True
    return False


def checkDraw():
    for row in board:
        if "" in row:
            return False
    return True


def buttonCallback(sender, appData, userData):
    global currentPlayer
    row, col = userData
    if board[row][col] == "":
        board[row][col] = currentPlayer
        dpg.set_value(sender, currentPlayer)
        if checkWin():
            dpg.configure_item("game_status", label=f"{currentPlayer} Wins!")
            dpg.disable_item("board_window")
        elif checkDraw():
            dpg.configure_item("game_status", label="It's a Draw!")
            dpg.disable_item("board_window")
        else:
            currentPlayer = "O" if currentPlayer == "X" else "X"
            dpg.configure_item("game_status", label=f"{currentPlayer}'s Turn")


def resetGame():
    global board, currentPlayer
    board = [["" for _ in range(3)] for _ in range(3)]
    currentPlayer = "X"
    dpg.configure_item("game_status", label="X's Turn")
    for i in range(3):
        for j in range(3):
            dpg.set_value(f"btn_{i}_{j}", "")
    dpg.enable_item("board_window")


with dpg.window(label="Tic Tac Toe", tag="board_window"):
    for i in range(3):
        with dpg.group(horizontal=True):
            for j in range(3):
                dpg.add_button(
                    label="",
                    tag=f"btn_{i}_{j}",
                    callback=buttonCallback,
                    userData=(i, j),
                    width=100,
                    height=100,
                )

dpg.add_button(label="Reset Game", callback=resetGame)
dpg.add_label_text(label="X's Turn", tag="game_status")

dpg.start_dearpygui()
