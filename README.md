# Tic-Tac-Toe-game-with-7-search-algorithms
This Python code uses Tkinter to create a Tic-Tac-Toe game where players can play against a computer employing search algorithms like DFS, BFS, IDDFS UCS, Greedy Search, and A*. 

## DFS
### Function Purpose:

The DFS function aims to determine if the computer player can reach a specific target cell on the Tic-Tac-Toe board through a series of moves.

### Data Structures:
It uses a boolean list visited to track whether each cell on the board has been visited during the DFS traversal.
A stack is employed to facilitate the depth-first exploration of possible moves.

### DFS Algorithm:
*The algorithm starts with the source cell (src) pushed onto the stack and marked as visited.
*It enters a loop, popping cells from the stack.
*If the popped cell is the target, the function returns True.
*Otherwise, it explores neighboring unvisited and empty cells, pushing them onto the stack.
*The loop continues until either the target is found or all possible moves are explored.

### Return Value:
*If the target is reached, the function returns True, indicating that the target cell is reachable through valid moves.
*If the target is not reached, the function returns False.

### Context:
This DFS function is likely used to check if the computer can achieve a winning state through a sequence of moves on the Tic-Tac-Toe board, influencing the computer's decision for its next move.

![image](https://github.com/Arwa-Fawzy/Tic-Tac-Toe-game-with-6-search-algorithms/assets/101527083/1b5a097d-f28a-44ae-a99d-6dc7be654122)

## BFS
### Function Purpose:
The BFS function is designed to find the shortest path from the source cell to a target depth on the Tic-Tac-Toe board using Breadth-First Search.

### Data Structures:
It utilizes a queue to manage the breadth-first exploration of possible moves.

### BFS Algorithm:
*The algorithm starts with the initial board state and depth pushed into a queue.
*It enters a loop, dequeuing elements and checking if the target depth is reached.
*If the target depth is reached, the function returns the current board state.
*Otherwise, it generates possible next moves by placing the computer's symbol in empty cells and enqueues them.
*The loop continues until the target depth is achieved or the queue is empty.

### Return Value:
If the target depth is reached, the function returns the board state representing the shortest path.
If the target depth is not reached, it returns None.

### Context:
This BFS function is likely used to find the optimal sequence of moves for the computer to reach a specific depth on the Tic-Tac-Toe board, influencing the computer's decision for its next move.

![image](https://github.com/Arwa-Fawzy/Tic-Tac-Toe-game-with-6-search-algorithms/assets/101527083/d1ef8026-c4c9-4fbe-bd27-76c74bb0e463)


## IDDFS

### Function Purpose:
The iddfs function implements Iterative Deepening Depth-First Search to find a move for the computer player on the Tic-Tac-Toe board.

### Algorithm Overview:
The function performs a series of depth-limited DFS searches, gradually increasing the depth limit until a valid move is found.
It iterates through all possible moves (empty cells) and checks if a winning state can be reached within a certain depth limit.

### DFS Implementation:
The dls (Depth-Limited Search) function is called to perform a depth-limited DFS from the current move, checking if a winning state is reachable within a given depth limit.
 
### Return Value:
If a winning move is found within the depth limit, the function returns the index of that move.
If no winning move is found within the current depth limit, the function returns a random move from the remaining empty cells.

### Context:
This IDDFS function is likely used to find a move for the computer player that leads to a winning state on the Tic-Tac-Toe board. It balances depth-limited exploration with computational efficiency.


![image](https://github.com/Arwa-Fawzy/Tic-Tac-Toe-game-with-6-search-algorithms/assets/101527083/8c9bee6a-1abb-4721-a746-37b5301d6254)


## UCS

### Function Purpose:

The ucs_search function implements Uniform Cost Search to find an optimal move for the computer player on the Tic-Tac-Toe board.
Algorithm Overview:

UCS is a best-first search algorithm that expands nodes with the least cost, determined by a priority queue. In this context, the cost is the depth of the search.

### Implementation:

The function uses a priority queue (heap) to manage the search, where each node is a potential board state along with its cost and the current player.
It iteratively dequeues nodes, expanding the ones with the least cost (depth) first.

### DFS Exploration:

*The moving function generates possible moves (empty cells) on the current board.
*For each move, a new board state is created, and its cost is calculated based on the depth of the search.
*Nodes are added to the priority queue, prioritized by their cost.

### Return Value:

If a winning move is found during the search, the function returns the resulting board state.
If the search completes without finding a winning move, it returns the original board.

### Context:

This UCS function is likely used to find an optimal move for the computer player, considering the cost (depth) of reaching a potential winning state on the Tic-Tac-Toe board. It aims to balance efficiency with optimality.



## Greedy 

### Function Purpose:

The greedy function implements a Greedy Algorithm to find a move for the computer player on the Tic-Tac-Toe board.

### Algorithm Overview:

Greedy algorithms make locally optimal choices at each stage with the hope of finding a global optimum. In this context, the algorithm prioritizes moves that minimize the distance to the player's symbols on the board.

### Implementation:

*The function takes a list of empty cells as input, representing possible moves.
*It identifies the player's current positions on the board to calculate the distance to each empty cell.
*The move with the minimum distance to the player's symbols is chosen as the next move.

### Return Value:
The function returns the index of the selected move, representing the cell where the computer player will place its symbol.

### Context:
This Greedy Algorithm is likely used to guide the computer player to make a move that minimizes the distance to the player's symbols, aiming for a favorable position on the Tic-Tac-Toe board. It's a heuristic approach for decision-making.

![image](https://github.com/Arwa-Fawzy/Tic-Tac-Toe-game-with-6-search-algorithms/assets/101527083/9aa44a28-9b4b-413e-a192-eea02347f3b0)

## A*

### Function Purpose:
The A_star function implements the A* Algorithm to find an optimal move for the computer player on the Tic-Tac-Toe board.

### Algorithm Overview:
A* is an informed search algorithm that uses both the cost to reach a node and an estimate of the cost to reach the goal. In this context, the algorithm combines a heuristic function with the actual distance traveled.

### Implementation:
*The function takes a list of empty cells as input, representing possible moves.
*It assigns heuristic values to each empty cell, estimating their desirability.
*A combined score, incorporating both the heuristic value and the distance to the last player's move, is calculated for each cell.
*The move with the minimum combined score is chosen as the next move.

### Return Value:
The function returns the index of the selected move, representing the cell where the computer player will place its symbol.

### Context:
This A* Algorithm is likely used to guide the computer player to make a move that minimizes the combined cost of reaching a favorable position on the Tic-Tac-Toe board. It considers both the heuristic estimate and the actual distance traveled for decision-making.

![image](https://github.com/Arwa-Fawzy/Tic-Tac-Toe-game-with-6-search-algorithms/assets/101527083/21bedb80-04e9-43b9-a2c3-4dc10c5919b0)



