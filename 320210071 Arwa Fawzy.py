import tkinter as tk
from tkinter import messagebox
import random
import queue
import heapq


root = tk.Tk()
root.title("X-O Game")
root.geometry("320x400")

board = [" " for _ in range(9)]
player_symbol = "X"
computer_symbol = "O"
turn = "player"  

def is_game_over():
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    if " " not in board:
        return "tie"
    return None

def end_game(winner):
    if winner == "tie":
        messagebox.showinfo("X-O Game", "It's a tie!")
    else:
        messagebox.showinfo("X-O Game", f"{winner} wins!")
    root.destroy()

def BFS(initial_board, target_depth):
    queue = [(initial_board, 0)]
    
    while queue:
        current_board, depth = queue.pop(0)
        if depth == target_depth:
            return current_board
        
        empty_cells = [i for i, cell in enumerate(current_board) if cell == " "]
        for cell in empty_cells:
            next_board = current_board.copy()
            next_board[cell] = computer_symbol
            queue.append((next_board, depth + 1))
    
    return None


def player_move(cell):
    global turn
    if board[cell] == " " and turn == "player":
        board[cell] = player_symbol
        buttons[cell].config(image=img_x, state="disabled")
        winner = is_game_over()
        if winner:
            end_game(winner)
        else:
            turn = "computer"
            player_target=cell
            computer_move()
player_target =None
def computer_move():
    global turn, player_target
    empty_cells=[]
    for i in range(9):
        if board[i]==" ":
            empty_cells.append(i)
    if empty_cells and turn == "computer":
        #cell = iddfs() 
        #cell = greedy(empty_cells)
        #cell = A_star(empty_cells)
        #cell = DFS(0, 8)
        #cell=ucs_search(board,'O')
        
        """
        board[cell] = computer_symbol
        buttons[cell].config(image=img_o, state="disabled")
        winner=is_game_over()
        if winner:
            end_game(winner)
        else:
            turn="player"
        """
    
    
        
        target_depth = len(empty_cells)  # The depth to reach all filled cells
        root_board = board.copy()
        if player_target is not None:
            root_board[player_target] = player_symbol
        
        result_board = BFS(root_board, target_depth)
        
        
        if result_board is not None:
            for i in range(9):
                if board[i] != result_board[i]:
                    board[i] = result_board[i]
                    buttons[i].config(image=img_o, state="disabled")
                    break
        winner = is_game_over()
        if winner:
            end_game(winner)
        else:
            turn = "player"    
        
        cell=BFS(board,len(empty_cells))
        if cell:
            for i in range(9):
                if cell[i] == computer_symbol and board[i] == " ":
                    board[i] = computer_symbol
                    buttons[i].config(image=img_o, state="disabled")
                    winner = is_game_over()
                    if winner:
                        end_game(winner)
                    else:
                        turn = "player"
    
        
                        
def ucs_search(board, player):
    queue = [(0, board, player)]
    while queue:
        cost, current_board, current_player = heapq.heappop(queue)
        if is_game_over():
            return current_board
        moves = moving(current_board)
        next_player = "X" if current_player == "O" else "O"
        for move in moves:
            new_board = [row[:] for row in current_board]
            new_board[move[0]][move[1]] = current_player
            heapq.heappush(queue, (cost + 1, new_board, next_player))

    return board


def moving(current_board):
    moves = []
    for i in range(3):
        for j in range(3):
            if current_board[i][j] == " ":
                moves.append((i, j))
    return moves

board = [[" " for _ in range(3)] for _ in range(3)]


def dls(src, target, maxDepth):
    if src == target:
        return True
    if maxDepth <= 0:
        return False
    for i in range(9):
        if board[i] == " ":
            board[i] = computer_symbol
            if not dls(i, target, maxDepth - 1):
                board[i] = " "
                return True
            board[i] = " "
    return False

def iddfs():
    for i in range(9):
        if board[i] == " ":
            board[i] = computer_symbol
            if not dls(i, i, 9):  
                board[i] = " "
                return i
            board[i] = " "

    empty_cells = []
    for i in range(9):
        if board[i] == " ":
            empty_cells.append(i)
    return random.choice(empty_cells)

def greedy(empty_cells):
    player_positions = []
    for i, cell in enumerate(board):
        if cell == player_symbol:
            player_positions.append(i)

    best_move = None
    min_distance = float('inf')

    for cell in empty_cells:
        row, col = divmod(cell, 3)
        for player_cell in player_positions:
            player_row, player_col = divmod(player_cell, 3)
            distance = abs(row - player_row) + abs(col - player_col)

            if distance < min_distance:
                min_distance = distance
                best_move = cell

    return best_move

def A_star(empty_cells):
    heuristic_values = [
        1, 2, 3,
        4, 5, 6,
        7, 8, 9
    ]
    best_move = None
    min_combined_score = float('inf')
    for cell in empty_cells:
        heuristic = heuristic_values[cell]
        row, col = divmod(cell, 3)
        last_player_row, last_player_col = divmod(board.index(player_symbol), 3)
        distance = abs(row - last_player_row) + abs(col - last_player_col)
        combined_score = heuristic + distance
        if combined_score < min_combined_score:
            min_combined_score = combined_score
            best_move = cell
    return best_move

def DFS(src, target):
    visited = [False] * 9

    stack = []

    stack.append(src)
    visited[src] = True

    while stack:
        src = stack[-1]
        stack.pop()

        if src == target:
            return True

        for i in range(9): 
            if not visited[i] and board[i] == " ":
                stack.append(i)
                visited[i] = True

    return False


def reset_game():
    global board, turn
    board = [" " for _ in range(9)]
    turn = "player"
    for button in buttons:
        button.config(image=img_back, state="active")
        
    player_target = None

img_x = tk.PhotoImage(file="G:/CS/5th/intelligent systems/project1/x.png")
img_o = tk.PhotoImage(file="G:/CS/5th/intelligent systems/project1/oo.png")
img_back = tk.PhotoImage(file="G:/CS/5th/intelligent systems/project1/back.png")


buttons = []
for i in range(9):
    row, col = divmod(i, 3)
    button = tk.Button(root, image=img_back, width=100, height=100, command=lambda i=i: player_move(i))
    button.grid(row=row, column=col)
    buttons.append(button)

reset = tk.Button(root, text="Reset", command=reset_game, bg="red", fg="white")
reset.config(font=("Arial", 14))
reset.grid(row=3, column=0, columnspan=3, pady=10)

reset_game()

root.mainloop()
