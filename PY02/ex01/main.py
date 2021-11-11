def what_are_the_vars(*args, **kwargs):
	"""
    ...
	"""
	var_nb = 0
	ret_class = ObjectC()
	for elem in args:
		setattr(ret_class, "var_" + str(var_nb), elem)
		var_nb += 1
	for key, value in kwargs.items():
		if hasattr(ret_class, key):
			return None
		else:
			setattr(ret_class, key, value)
	return ret_class



class ObjectC(object):
	def __init__(self):
		pass
	
def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != "_":
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)