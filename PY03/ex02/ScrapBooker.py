from matplotlib import artist
import numpy


import numpy as np
from numpy.lib.arraysetops import isin

class ScrapBooker:

	def crop(self, array, dim, position=(0,0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width oof the image) from the coordinates given by position arguments.
		Args:
			array: numpy.ndarray
			dim: tuple of 2 integers.
			position: tuple of 2 integers.
		Returns:
			new_arr: the cropped numpy.ndarray.
			None otherwise (combinaison of parameters not incompatible).
		Raises:
			This function should not raise any Exception.
		"""
		#PROTEGER SI ELEM PAS DES INT
		if not isinstance(array, np.ndarray) or not isinstance(dim, tuple) \
			or not isinstance(position, tuple) or not all(isinstance(x, int) for x in dim) \
				or not all(isinstance(x, int) for x in position) or dim[0] < 0 or dim[1] < 0 or position[0] < 0 or position[1] < 0:
			return None
		#elif:
		#	return None
		else:
			return(np.array(array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]))

	def thin(self, array, n, axis): 
		"""
		Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
		Args:
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
			(depending of axis value).
		axis: positive non null integer.
		Returns:
		new_arr: thined numpy.ndarray.
		None otherwise (combinaison of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int) or (axis != 0 and axis != 1) or n <= 0:
			return None
		elif (axis == 0 and n >= np.shape(array)[1]) or (axis == 1 and n >= np.shape(array)[0]):
			return None
		elif (axis == 0):
			copy = list(array)
			ret = []
			for i, elem in enumerate(array):
				ret2 = []
				for j, elem2 in enumerate(elem):
					if j % n != 0: 
						ret2.append(elem2)
				ret.append(ret2)	
			return(np.array(ret))
		else:
			copy = list(array)
			ret = []
			for i, elem in enumerate(array):
				if i % n != 0:
					ret.append(elem)
			return(np.array(ret))

	def juxtapose(self, array, n, axis): 
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Returns:
		new_arr: juxtaposed numpy.ndarray.
		None otherwise (combinaison of parameters not incompatible).
		Raises:
		This function should not raise any Exception.
		"""
		if not isinstance(array, np.ndarray) or not isinstance(n, int) or not isinstance(axis, int) or (axis != 0 and axis != 1) or n <= 0:
			return None
		elif (axis == 0):
			ret = []
			return (np.array(ret))
		elif (axis == 1):
			ret = []
			for i, elem in enumerate(array):
				ret2 = []
				count = 0
				while (count < n):
					for i, elem2 in enumerate(elem):
						ret2.append(elem2)
					count+=1
				ret.append(ret2)
			return (np.array(ret))
		
	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
			array: numpy.ndarray.
			dim: tuple of 2 integers.
		Returns:
			new_arr: mosaic numpy.ndarray.
			None otherwise (combinaison of parameters not incompatible).
		Raises:
			This function should not raise any Exception.
			"""
	
   
spb = ScrapBooker()
#arr1 = np.arange(0,25).reshape(5,5)
#print(arr1, end="\n\n")
#rint(spb.crop(arr1, (3,1),(1,0)), end="\n\n")
#print(spb.thin(arr1, 2, 0))
#print(spb.juxtapose(arr1, 2, 1))

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))
