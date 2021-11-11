from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

string1="Bonjour Monde"
list1=["Bonjour", "Monde", "C'est bien moi", "jeune", "et libre"]
tup1=[1, 9, 10, 5]

try:
	tup2 = ft_map(lambda elem : elem + 10, tup1)
	print((tup2))
except ValueError as err:
	print(err.args)

try:
	print(list(ft_filter(lambda elem : len(elem) > 5, list1)))
except ValueError as err:
	print(err.args)

try:
	r1 = reduce(lambda a, b : a * b, [1, 1, 33, 444, 555])
	r2 = ft_reduce(lambda a, b: a * b, [1, 1, 33, 444, 555])
	print(r1)
	print(r2)
except ValueError as err:
	print(err.args)