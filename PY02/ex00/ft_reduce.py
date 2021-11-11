def ft_reduce(function_to_apply, iterable):
	try:
		copy = next(iter(iterable))
		for i in range(1, len(iterable)):
			copy = function_to_apply(copy, iterable[i])
		return copy
	except TypeError:
		raise ValueError("Map:Cannot Apply that function to that type")