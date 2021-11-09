import sys

morse = {
	' ' : '/', '-' : '-----', '1' : ".----", '2' : '..---', '3' : '...--', '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.',\
		'A' : '.-', 'B' : '-...', 'C' : '-.-.', 'D' : '-..', 'E' : '.', 'F' : '..-.', 'G' : '--.', 'H' : '....', 'I' : '..', 'J' : '.---', 'K' : '-.-',\
			'L' : '.-..', 'M' : '--', 'N' : '-.', 'O' : '---', 'P' : '.--.', 'Q' : '--.-', 'R' : '.-.', 'S' : '...', 'T' : '-', 'U' : '..-', 'V' : '...-',\
				'W' : '.--', 'X' : '-..-', 'Y' : '-.--', 'Z' : '--..'
		}

for word in sys.argv[1:]:
	for letter in word:
		if not letter.isalnum() and not letter.isspace():
			print("ERROR")
			quit()

for sentence in sys.argv[1:]:
	sentence = sentence.strip()
	for word in sentence:
		for letter in word:
			print(morse[letter.upper()], end=' ')
	print('/', end='')
