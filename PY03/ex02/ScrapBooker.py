from matplotlib import artist
import numpy


import numpy as np
from numpy.lib.arraysetops import isin

class ScrapBooker:

	def crop(self, array, dim, position=(0,0)):
		if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) \
			or not isinstance(position, tuple) or not all(isinstance(x, int) for x in dim) \
				or not all(isinstance(x, int) for x in position) or dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0:
			return None
		else:
			shape = np.shape(array)
			if position[0] >= shape[0] or position[1] >= shape[1]:
				return None
			if position[0] + dim[0] >= shape[0] or position[1] + dim[1] >= shape[1]:
				return None
			return array[position[0]: position[0] + dim[0], position[1]: position[1] + dim[1]]

	def thin(self, array, n, axis): 
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int) or (axis != 0 and axis != 1) or n <= 0:
			return None
		elif (axis == 0 and n >= np.shape(array)[1]) or (axis == 1 and n >= np.shape(array)[0]):
			return None
		elif (axis == 0):
			new_tab = array
			x = 1
			while (n - 1) * x < np.shape(new_tab)[1]:
				new_tab = np.delete(new_tab, (n - 1) * x, 1)
				x += 1
			return new_tab
		elif axis == 1:
			new_tab = array
			x = 1
			print(np.shape(new_tab)[0])
			while (n - 1) * x < np.shape(new_tab)[0]:
				new_tab = np.delete(new_tab, (n - 1) * x, 0)
				x += 1
			return new_tab

	def juxtapose(self, array, n, axis): 
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int) or (axis != 0 and axis != 1) or n <= 0:
			return None
		else:
			old_shape = np.shape(array)
			if (axis == 0):
				new_shape = (old_shape[0] * n, old_shape[1])
				new_array = np.zeros(new_shape)
				i = 0
				while i < new_shape[0]:
					j = 0
					while j < new_shape[1]:
						new_array[i, j] = array[i % n, j]
						j += 1
					i += 1
			elif axis == 1:
				new_shape = (old_shape[0], old_shape[1] * n)
				new_array = np.zeros(new_shape)
				i = 0
				while i < new_shape[0]:
					j = 0
					while j < new_shape[1]:
						new_array[i, j] = array[i, j % n]
						j += 1
					i += 1
			return (new_array)
		
	def mosaic(self, array, dim):
		if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) \
		 or not all(isinstance(x, int) for x in dim) \
			 or dim[0] < 0 or dim[1] < 0:
			return None
		else:
			new_array = self.juxtapose(array, dim[0], 0)
			new_array = self.juxtapose(new_array, dim[1], 1)
			return (new_array)
	
   
spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(arr1, end="\n\n")
print(spb.crop(arr1, (3,1),(1,0)), end="\n\n")


arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(arr2, end="\n\n")
print(spb.thin(arr2,3,0), end="\n\n")

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(arr3, end="\n\n")
print(spb.mosaic(arr3, (3, 3)))
