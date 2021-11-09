import random

count = 0
nb = random.randint(1, 99)

print("This is an interactive guessing game!\n\
You have to enter a number between 1 and 99 to find out the secret number.\n\
Type 'exit' to end the game.\n\
Good luck!", end="\n\n")

while 1:
	guess = input("What's your guess between 1 and 99?\n>>")
	if guess.strip() == "exit":
		print("Goodbye!")
		quit()
	if not guess.strip().isnumeric():
		print("That's not a number.")
	else:
		count+=1
		nb_input = int(guess.strip())
		if (nb_input == nb == 42):
			print("The answer to the ultimate question of life, the universe and everything is 42.")
		if nb_input == nb and count > 1:
			print("Congratulations, you've got it!\nYou won in %d attempts!" % count)
			quit()
		elif nb_input == nb and count == 1:
			print("Congratulations! You got it on your first try!")
			quit()
		elif nb_input > nb:
			print("Too high!")
		else:
			print("Too low!")