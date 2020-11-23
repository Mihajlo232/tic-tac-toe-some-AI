from os import system
import time
from math import inf as infinity


board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def print_board(board):
	print(" ", board[0], "|", " ", board[1], " ",  "|", " ", board[2])
	print("----------------")
	print(" ", board[3], "|", " ", board[4], " ",  "|", " ", board[5])
	print("----------------")
	print(" ", board[6], "|", " ", board[7], " ", "|", " ", board[8])


def evaluate(state):
	if winner(state, "O"):
		score = +1
	elif winner(state, "X"):
		score = -1
	else:
		score = 0
	return score


def available_spots(board):
	result = []
	for i, j in enumerate(board):
		if j == "_":
			result.append(i)
	return result

def winner(state, player):
	win_state = [[state[0], state[1], state[2]],
	[state[3], state[4], state[5]],
	[state[6], state[7], state[8]],
	[state[0], state[3], state[6]],
	[state[1], state[4], state[7]],
	[state[2], state[5], state[8]],
	[state[0], state[4], state[8]],
	[state[2], state[4], state[6]],
	]

	if [player, player, player] in win_state:
		return True
	else:
		return False


def game_over(state):
	return winner(state, "X") or winner(state, "O")


def minimax(board, depth, player):
	if player == "O":
		best = [-1, -infinity]
	else:
		best = [-1, infinity]

	if depth == 0 or game_over(board):
		score = evaluate(board)
		return [-1, score]

	for cell in available_spots(board):
		board[cell] = player

		if player == "O":
			score = minimax(board, depth -1, "X")
		else:
			score = minimax(board, depth -1, "O")
		board[cell] = "_"
		score[0] = cell
		if player == "O":
			if best[1] < score[1]:
				best = score
			else:
				if best[1] > score[1]:
					best = score

	return best


def human_input(board):
	
	depth = len(available_spots(board))
	if depth == 0 or game_over(board):
		return

	move = -1

	while move < 1 or move > 9:
		clean()
		print("Human's turn \n")
		print_board(board)
		move = int(input("Enter position (1...9): "))
		
		if move <= 9 and move >= 1:
			if board[move-1] == "_":
				move -= 1
				board[move] = "X"
				print_board(board)
				return
		else:
			print("Not available position!")
			move = -1 
			time.sleep(1)
	
	else:
		print("bad move")
		move = -1


def clean():
    system("cls")


def AI_move():
	depth = len(available_spots(board))

	if depth == 0 or game_over(board):
		return

	clean()

	print("AI's turn \n")
	move = minimax(board, depth, "O")
	board[move[0]] = "O"
	print_board(board)
	time.sleep(1)


def main(board):
	while len(available_spots(board)) > 0 and not game_over(board):
		human_input(board)
		AI_move()

	if winner(board, "X"):
		print("Human has won! GO HUMANS !")
		return 0 
	elif winner(board, "O"):
		print("AI won, of course!")
		return 0 
	else:
		print("Draw")
		return 0


if __name__ == "__main__":
	while True:
		main(board)
		board = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
		again = input("Do you want to play again? [y/n]: ")
		if again == "n":
			break
















































