# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameVars

# # set up some variables for player and AI lives
# player_lives = 1
# computer_lives = 1

# # choices is an array => an array is a container that can hold multiple values
# # arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc
# choices = ["rock", "paper", "scissors"]

# # set the computer variable to one of these choices (0, 1 or 2)
# computer = choices[randint(0, 2)]

# # set up the game loop so that we don't have to restart all the time
# player = False

while gameVars.player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", gameVars.computer_lives, "/",gameVars.total_lives,"\n")
	print("Player lives: ", gameVars.player_lives, "/",gameVars.total_lives,"\n")
	print("Choose your weapon!\n")
	print("**********************************")

	gameVars.player = input("choose rock, paper or scissors: ")
	gameVars.player = gameVars.player.lower()

	print("computer chose ", gameVars.computer, "\n")
	print("player chose ", gameVars.player, "\n")

	if gameVars.player.lower() == "quit":
		exit()
	elif gameVars.computer == gameVars.player:
		print("tie! no one wins, play again")

	elif gameVars.player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", gameVars.player, "\n")
			gameVars.player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", gameVars.player, "\n")
			player_lives = gameVars.player_lives - 1
		else:
			print("You win!", gameVars.player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	elif gameVars.player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", gameVars.player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", gameVars.player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")


	# handle all lives lost for gameVars.player or AI
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gameVars.player = False
		gameVars.computer = gameVars.choices[randint(0, 2)]	

