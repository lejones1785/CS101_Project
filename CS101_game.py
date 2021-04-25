#Select the game to play
from Rock_Paper_Scissors import play_rps

pick_game = int(input("Would you like to play a game? \n 1: Rock, Paper, Scissors\n 2: The Maze Adventure \n 3: Guess the Number \n"))


if pick_game == 1:
	play_rps()
else:
	print("please pick a game")
