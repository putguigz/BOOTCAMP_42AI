def ft_reduce(function_to_apply, iterable):
	try:
		for i in iterable:
			copy = (function_to_apply(i, i + 1))
		return copy 
	except TypeError:
		raise ValueError("Map:Cannot Apply that function to that type")