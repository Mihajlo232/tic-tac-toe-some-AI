import numpy as np

horizontal = "-----"
vertical = " | | "
i = 0

#table
while i < 5:
	i += 1
	if i == 2 or i == 4:
		
		print(horizontal) 
	else: 
		print(vertical)
game = [[0, 0, 0],
		[0, 0, 0],
		[0, 0, 0]]

user1 = 1
user2 = 2

set_r = ()
set_c = ()


def line_match(game):
	for i in range(3):
		set_r = set(game[i])
		if len(set_r) == 1 and game[i][0] != 0:
			return game[i][0]
	return 0


def diagonal_match(game):
	if game[1][1] != 0:
		if game[1][1] == game[0][0] == game[2][2]: 
			return game[1][1]
		elif game[1][1] == game[0][2] == game[2][0]:
			return game[1][1]	
	return 0


possible_input = [0, 1, 2]

def user_1_input(game):
	input_kords_user_1 = []
	input_kords_user_1_a = int(input("(1st player) Position x? "))
	input_kords_user_1_b = int(input("(1st player) Position y? "))
	if input_kords_user_1_a not in possible_input or input_kords_user_1_b not in possible_input:
		print("Error, invalid input.")


	else:	
		input_kords_user_1.append(input_kords_user_1_a)
		input_kords_user_1.append(input_kords_user_1_b)
	
		column = input_kords_user_1[0]
		row = input_kords_user_1[1]
		game[column][row] = 1


def user_2_input(game):
	input_kords_user_2 = []
	input_kords_user_2_a = int(input("(2nd player) Position x? "))
	input_kords_user_2_b = int(input("(2nd player) Position y? "))
	if input_kords_user_2_a not in possible_input or input_kords_user_2_b not in possible_input:
		print("Error, invalid input.")

	else:
		input_kords_user_2.append(input_kords_user_2_a)
		input_kords_user_2.append(input_kords_user_2_b)
	
		column = input_kords_user_2[0]
		row = input_kords_user_2[1]
		game[column][row] = 2



def game_runner(game):
	i = 0
	backuper = 0
	stop = 0 
	for i in range(9):
		i += 1
		print("move:", i)

	 	#baasckup loop 			

		if i / 2 == 1 or i / 2 == 2 or i / 2 == 3 or i / 2 == 4:
		
			user_2_input(game)
			print(game)
		else:
			user_1_input(game)
			print(game)
			
		#for j in game:
		#	for x in j:
		#		if x == 1 or x == 2:
		#			backuper += 1
		#if backuper != i:
		#	print("ERROR")
		#	print("backuper:", backuper)
		#else:
		#	print("backuper:", backuper)
		#	print("i:", i)
		#	continue	

		for n in range(3, 10):
			if n == i:
				line_match(game)
				diagonal_match(game)
	
				#line win
				if line_match(game) == 1:			
					print (str(line_match(game)) + str("Player one has won - row win!"))
					stop = 1		
				if line_match(game) == 2:			
					print (str(line_match(game)) + str("Player two has won - row win!"))
					stop = 1
				#line reverse win
				if line_match(np.transpose(game)) == 1:
					print (str(line_match(np.transpose(game))) + str("Player one has won - column win!"))
					stop = 1
				if line_match(np.transpose(game)) == 2:
					print (str(line_match(np.transpose(game))) + str("Player two has won - column win!"))
					stop = 1
				#diagonal win
				if diagonal_match(game) == 1:
					print (str(diagonal_match(game)) + str(" Player one has won - diagonal win!"))
					stop = 1
				if diagonal_match(game) == 2:
					print (str(diagonal_match(game)) + str(" Player two has won - diagonal win!"))
					stop = 1
				elif i == 9 and diagonal_match(game) == 0 and line_match(np.transpose(game)) == 0 and line_match(game) == 0:
					print("No winner in this game!")
		if stop > 0:
			print("GG")
			break
		else:
			continue

#I love two monitors - i really like it! looks great!



game_runner(game)





#
#
#
#
#
#
#
#
#