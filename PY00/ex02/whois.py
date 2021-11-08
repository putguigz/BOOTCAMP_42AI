import sys

if len(sys.argv) < 2:
	quit()

if len(sys.argv) > 2:
	print("ERROR")
	quit()

if sys.argv[1].isdigit() == False:
	print("ERROR")
	quit()

nb = int(sys.argv[1])

if nb == 0:
	print("I'm Zero.")
elif nb % 2 == 0:
	print("I'm Even.")
else:
	print("I'm Odd.")
