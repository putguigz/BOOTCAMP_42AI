
def ft_map(function_to_apply, iterable):
	try:
		for i in iterable:
			yield function_to_apply(i)
	except TypeError:
		raise ValueError("Map:Cannot Apply that function to that type")
	

