t = (19, 42, 21)

print("The", len(t), "numbers are:", end= ' ')

for elem in t:
	if elem != t[-1]:
		print(elem, end=', ')
	else:
		print(elem)
