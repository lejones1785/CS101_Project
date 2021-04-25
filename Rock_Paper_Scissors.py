
from random import randint

#Define game play
def play_rps():
	comp_score = 0
	user_score = 0
	play_round = 0

#start the game
	while play_round < 3:
#get computer play		
		comp_play = randint(1, 3)

		if comp_play == 1:
			comp_play = "rock"
		elif comp_play == 2:
			comp_play = "paper"
		elif comp_play == 3:
			comp_play = "scissors"

#Determine user play		
		user_play = input("What is your choice?\n rock \n paper \n scissors \n")
		
		if user_play.lower() == "rock" or user_play.lower() == "paper" or user_play.lower() == "scissors":
			user_play = user_play.lower()
		else:
			input("You play was invalid, try agian. \n What is your choice?\n rock \n paper \n scissors \n")

#Determine the winner
		if user_play == "rock" and comp_play =="scissors":
			user_score += 1
			print(f"You played {user_play} and the computer played {comp_play}.\n Rock crushes scissors, you win!\n")
		elif user_play == "rock" and comp_play == "paper":
			comp_score += 1
			print(f"You played {user_play} and the computer played {comp_play}.\n Paper covers rock, you lose.\n")
		elif user_play == "paper" and comp_play == "rock":
			user_score += 1
			print(f"You played {user_play} and the computer played {comp_play}.\n Paper covers rock, you win!\n")
		elif user_play == "paper" and comp_play == "scissors":
			comp_score +=1
			print(f"You played {user_play} and the computer played {comp_play}.\n Scissors cut paper, you lose.\n")
		elif user_play == "scissors" and comp_play == "paper":
			user_score += 1
			print(f"You played {user_play} and the computer played {comp_play}.\n Scissors cuts paper, you win!\n")
		elif user_play == "scissors" and comp_play == "rock":
			comp_score += 1
			print(f"You played {user_play} and the computer played {comp_play}.\n Rock crushes scissors, you lose!\n")
		elif user_play == comp_play:
			print(f"You played {user_play} and the computer played {comp_play}.\n The round was a tie, play again!\n")
		play_round += 1
	
	if comp_score < user_score:
		print(f"The final score was \n Player: {user_score} \n Computer: {comp_score} \nYou win the game!")
	elif comp_score > user_score:
		print(f"The final score was \n Player: {user_score} \n Computer: {comp_score} \nSorry you lost, try again!")
	else:
		print(f"The final score was \n Player: {user_score} \n Computer: {comp_score} \nThe game was a tie, try again!")


