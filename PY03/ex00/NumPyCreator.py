from typing import Iterable
import numpy as np
import random

class NumPyCreator:
	@staticmethod
	def from_list(lst):
		'''takes a list or nested list and 
		returns its corresponding Numpy array,'''
		if not isinstance(lst, list):
			return None
		else:
			type_0 = type(lst[0])
			size_0 = len(lst[0])
			for elem in lst:
				if len(elem) != size_0 or not isinstance(elem, type_0):
					return None
			return(np.array(lst))

	@staticmethod
	def from_tuple( tpl):
		'''takes a tuple or nested tuple and 
		returns its corresponding Numpy array,'''
		if not isinstance(tpl, tuple):
			return None
		else:
			return np.array(tpl)

	@staticmethod
	def from_iterable(itr): 
		'''takes an iterable and returns an array 
		which contains all of its elements'''
		if not isinstance(itr, Iterable):
			return None
		else:
			return np.array(list(itr))

	@staticmethod
	def from_shape(shape, value=0): 
		'''returns an array filled with the same value, 
		The first argument is a tuple which specifies the
		 shape of the array, and the second argument specifies 
		 the value of all the elements. This value must be 0 by default,
		'''
		if not isinstance(shape, tuple) or not isinstance(value, (int, float)) or not isinstance(shape[0], int) or not isinstance(shape[1], int) or shape[0] <= 0 or shape[1] <= 0:
			return None
		else:
			return np.array([[value for x in range(shape[1])] for y in range(shape[0])])
	
	@staticmethod
	def random(shape): 
		'''returns an array filled with random values, It takes as an argument 
		a tuple which specifies the shape of the array,'''
		if not isinstance(shape, tuple) or not isinstance(shape[0], int) or not isinstance(shape[1], int) or shape[0] <= 0 or shape[1] <= 0:
			return None
		else:
			return np.array([[random.random() for x in range(shape[1])] for y in range(shape[0])])
	
	@staticmethod
	def identity(n):
		'''returns an array representing the identity matrix of size n.'''
		if not isinstance(n, int) or n <= 0:
			return None
		else:
			return np.identity(n)