class Vector:
	def __init__(self, lst):
		if isinstance(lst, int):
			if lst < 0:
				raise ValueError("0 >= <value> : forbidden to init Vector")
			self.values = []
			for i in range(lst):
				self.values.append([float(i)])
		elif isinstance(lst, tuple):
			if len(lst) != 2:
				raise ValueError("Wrong Range size")
			if not isinstance(lst[0], int) or not isinstance(lst[1], int):
				raise ValueError("Tuple is not composed of ints")
			if lst[1] - lst[0] == 0:
				raise ValueError("Size of 0 list is forbidden")
			self.values = []
			r1 = range(lst[0], lst[1])
			print(r1)
			for i in r1:
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
		else:
			raise ValueError("Wrong type of global input")
		nb_list = sum(isinstance(x, list) for x in self.values)
		if nb_list == 0:
			nb_list = 1
		if nb_list == 1:
			nb_float = sum(isinstance(x, float) for x in self.values)
		else:
			nb_float = 1
		self.shape = (nb_list, nb_float)
		
			
	def __add__(self, rhs):
		if rhs == 0:
			return self
		if not isinstance(rhs, Vector):
			raise ValueError("elem in operation not of Vector type.")
		if self.shape != rhs.shape:
			raise ValueError("elems doesn't have the same dimension")
		new_list = []
		if (self.shape[0] == 1):
			for i in range(self.shape[1]):
				new_list.append(self.values[i] + rhs.values[i])
		else:
			for i in range(self.shape[0]):
				new_list.append([self.values[i][0] + rhs.values[i][0]])
		return (Vector(new_list))

	def __radd__(self, rhs):
			return self.__add__(rhs)

	def __sub__(self, rhs):
		if rhs == 0:
			return self
		if not isinstance(rhs, Vector):
			raise ValueError("elem in operation not of Vector type.")
		if self.shape != rhs.shape:
			raise ValueError("elems doesn't have the same dimension")
		return (self.__add__(rhs.__mul__(-1)))

	def __rsub__(self, rhs):
		return self.__sub__(rhs)

	def __truediv__(self, rhs):
		if not isinstance(rhs, (int, float)):
			raise ValueError("Scalar is not int nor float")
		if rhs == 0:
			raise ValueError("Cannot divide by 0")
		new_list = []
		if (self.shape[0] == 1):
			for i in range(self.shape[1]):
				new_list.append(self.values[i] / rhs)
		else:
			for i in range(self.shape[0]):
				new_list.append([self.values[i][0] / rhs])
		return (Vector(new_list))
		

	def __rtruediv__(self, rhs):
		if isinstance(rhs, (int, float)):
			raise ValueError("A scalar cannot be divided by a Vector")
	
	def __mul__(self, rhs):
		if not isinstance(rhs, (int, float)):
			raise ValueError("Scalar is not int nor float")
		new_list = []
		if (self.shape[0] == 1):
			for i in range(self.shape[1]):
				new_list.append(self.values[i] * rhs)
		else:
			for i in range(self.shape[0]):
				new_list.append([self.values[i][0] * rhs])
		return (Vector(new_list))
		

	def __rmul__(self, rhs):
		return self.__mul__(rhs)
	
	def __str__(self):
		return f"Here is the content of class:\nShape = {self.shape}\nValue = {self.values}"

	def __repr__(self):
		return f"Vector(shape={self.shape} value={self.values})"

	def dot(self, rhs):
		if not isinstance(rhs, Vector):
			raise ValueError("Right elem is not of type Vector")
		if self.shape != rhs.shape:
			raise ValueError("Vectors are not of same dimension")
		new_list = []
		result = 0
		if (self.shape[0] == 1):
			for i in range(self.shape[1]):
				new_list.append(self.values[i] * rhs.values[i])
			for i in range(len(new_list)):
				result += new_list[i]
		else:
			for i in range(self.shape[0]):
				new_list.append([self.values[i][0] * rhs.values[i][0]])
			for i in range(len(new_list)):
				result += new_list[i][0]	
		return (result)
	
	def T(self):
		new_list = []
		if (self.shape[0] == 1):
			for i in range(self.shape[1]):
				new_list.append([self.values[i]])
		else:
			for i in range(self.shape[0]):
				new_list.append(self.values[i][0])
		return (Vector(new_list))

try:
	test = Vector([[1.0], [2.0], [3.0], [4.0], [5.0]])
	test2 = Vector([[5.0], [4.0], [3.0], [2.0], [1.0]])
	test3 = Vector([1.0, 2.0, 3.0, 4.0, 5.0])
	test4 = Vector([5.0, 4.0, 3.0, 2.0, 1.0])

	print(test2.T())
except ValueError as err:
	print(err.args)