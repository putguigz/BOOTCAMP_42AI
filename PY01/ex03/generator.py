from typing import Text
import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if not isinstance(text, str):
		raise ValueError("ERROR")

	splited = text.split(sep)
	if option == None or option == "ordered":
		for word in splited:
			yield word
	elif option == "unique":
		new_list = []
		for word in splited:
			if word not in new_list:
				new_list.append(word)
		for word in new_list:
			yield word
	elif option == "shuffle":
		lst_random = random.sample(range(len(splited)), len(splited))
		for i in lst_random:
			yield splited[i]
	else:
		raise ValueError("ERROR")

text = "Lorem Ipsum Lorem Ipsum"

for word in generator(text, option="unique"):
	print(word)