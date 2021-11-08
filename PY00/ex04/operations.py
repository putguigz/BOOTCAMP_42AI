import sys

error_str = "Usage: python operations.py <number1> <number2>\nExample:\n	python operations.py 10 3"

def	add(a, b):
	print('{0: <12}'.format("Sum:"), a + b)
	return a + b

def sub(a, b):
	print('{0: <12}'.format("Difference:"), a - b)
	return a - b

def mult(a, b):
	print('{0: <12}'.format("Product:"), a * b)
	return a * b

def div(a, b):
	print('{0: <12}'.format("Quotient:"), end='')
	if b == 0:
		print("ERROR (div by zero)")
		return "ERROR (div by zero)"
	else:
		print(a / b)
		return a / b


def mod(a, b):
	print('{0: <12}'.format("Remainder:"), end='')
	if b == 0:	
		print("ERROR (modulo by zero)")
		return "ERROR (modulo by zero)"
	else:
		print(a % b)
		return a * b

def results(a, b):
	return ((add(a, b), sub(a, b), mult(a, b), div(a, b), mod(a, b)))

if len(sys.argv) != 3:
	print(error_str)
	quit()

if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
	print("InputError: only numbers\n\n", error_str)
	quit()

a = int(sys.argv[1])
b = int(sys.argv[2])

results(a, b)
