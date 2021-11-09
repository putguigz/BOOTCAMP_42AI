class Vector:
	def __init__(self, lst):
		if isinstance(lst, int):
			if lst < 0:
				raise ValueError("0 >= <value> : forbidden to init Vector")
			self.values = []
			for i in range(lst):
				self.values.append([float(i)])
		elif isinstance(lst, range):
			if len(lst) == 0:
				raise ValueError("Size of 0 list is forbidden")
			self.values = []
			for i in lst:
				print(i)
				self.values.append([float(i)])
		elif isinstance(lst, list):
			if len(lst) == 0:
				raise ValueError("Empty list is forbidden")

			nb_floats = sum((isinstance(x, float) for x in lst))
			nb_lists = sum((isinstance(y, list) for y in lst))
			if not ((nb_floats != 0 and nb_lists == 0) or (nb_floats == 0 and nb_lists != 0)):
				raise ValueError("list is inconsistent in type")

			for sub_elem in lst:
				if isinstance(sub_elem, list):
					if len(sub_elem) > 1:
						raise ValueError("list of list must be of dimension 1")
					for sub_sub_elem in sub_elem:
						if not isinstance(sub_sub_elem, float):
							raise ValueError("Not floats inside list of list")	
			self.values = lst
		print(sum(isinstance(x, list) for x in self.values))
			
#	def __add__(self, rhs):
#		
#	def __radd__(self, rhs):
#
#	def __sub__(self, rhs):
#
#	def __rsub__(self, rhs):	
#
#	def __truediv__(self, rhs):
#
#	def __rtruediv__(self, rhs):
#
#	def __mul__(self, rhs):
#
#	def __rmul__(self, rhs):
#
#	def __str__(self, rhs):
#
#	def __repr__(self, rhs):

try:
	test = Vector([[0.0], [1.0], [2.0], [3.0]])
	print(test.values)
	#print(test.shape)
except ValueError as err:
	print(err.args)