class Evaluator:
	@staticmethod
	def zip_evaluate(words, coefs):
		if len(words) != len(coefs):
			return -1
		if not all(isinstance(x, str) for x in words):
			print("Words tab is not made only of strings")
			return -1
		if not all(isinstance(x, int) for x in coefs):
			print("Coefs tab is not made only of ints")
			return -1
		zipped = zip(words, coefs)
		result = sum((len(ite[0]) * ite[1]) for ite in zipped)
		return result

	@staticmethod
	def enumerate_evaluate(words, coefs):
		if len(words) != len(coefs):
			return -1
		if not all(isinstance(x, str) for x in words):
			print("Words tab is not made only of strings")
			return -1
		if not all(isinstance(x, int) for x in coefs):
			print("Coefs tab is not made only of ints")
			return -1
		result = sum((len(value) * coefs[counter]) for counter, value in enumerate(words))
		return result



text = ["Hellodfdsfsd", "1236712894616489126", "This", "is", "Me"]
coefs = [1000, 10000, 1, 1, 100]

try:
	print(Evaluator.zip_evaluate(text, coefs))
	print(Evaluator.enumerate_evaluate(text, coefs))
except ValueError as err:
	print(err.args)