import sys

morse = {
	    'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-', 'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-', 'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..'
		}

for word in sys.argv[1:]:
	if not word.isalnum() or not word.isupper():
		print("ERROR")
		quit()

for word in sys.argv[1:]:
		for letter in word:
			print(morse[letter], end=' ')

