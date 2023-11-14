# MyPygame
pygame.Puzzle.Game

#This is a game where number rannging from 1-9, in tiles repectivley, will be shuffled and you will have to rearrange it in a correct order.

1.KEY FUNCTIONALITY

A. The game board is automtically generated with a numbered tiles of 4*4 in a solved state.

B. Can randomly shuffle the tiles, as soon as you enter the game, and creates a new puzzle.

C. Allow tiles adjacent to the blannk space to smoothly slide into that space through arrow keys or mouse click.

D. Contains logic to recursively solve the board using optimal number moves.

E. Checks if the board is in the solved state and then displays a 'SOLVED!' message if solved in a correct order.

F. Sliding slides, shuffling and solving have smooth animations.

G. There is a on-screen clickable buttons to reset, get new puzzle or solve automatically.

#All in all, the key functionality cover game generation, sliding logic, solving animations and interactivity which are basically the core of the playable puzzle game.

2.WRITING TEST CASES

A. Game Board Generation.
    - Its normal successful operation is generating a standard 4*4 game board and verifying that it contains a value of 1-15 in a correct order with one blank space.
		
  Edge Cases: Generating a board with 0 row or columns, verify it raises an error or returns a default 1x1 board.
	
  Data Validation: Pass rows but not columns or vice versa, verify fails or uses defaults.
