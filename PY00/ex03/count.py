import fileinput
import string

def text_analyzer(*args):
	"""This function counts the number of upper characters, lower characters, punctuation and spaces in a given text."""
	upper_nb = 0
	lower_nb = 0
	punct_nb = 0
	sp_nb = 0

	if len(args) > 1:
		print("ERROR")
		return
	
	if len(args) == 0:
		var = input("What is the text to analyse? \n")
	var = args[0]	
	for c in var:
		if c.isupper():
			upper_nb += 1
		if c.islower():
			lower_nb += 1
		if c in string.punctuation:
			punct_nb += 1
		if c.isspace():
			sp_nb += 1

	print("The text contains ", len(args), "characters:")
	print(upper_nb, " upper letters")
	print(lower_nb, " lower letters")
	print(punct_nb, " punctuation marks")
	print(sp_nb, " spaces letters")
