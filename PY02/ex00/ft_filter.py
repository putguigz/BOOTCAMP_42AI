
def ft_filter(function_to_apply, iterable):
	try:
		for i in iterable:
			if function_to_apply(i):
				yield i
	except TypeError:
		raise ValueError("Map:Cannot Apply that function to that type")
