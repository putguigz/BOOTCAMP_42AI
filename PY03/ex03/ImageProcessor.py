from matplotlib import image
from matplotlib import pyplot
import numpy as np
import os

class ImageProcessor:

	@staticmethod
	def load(path):
		try:
			if os.stat(path).st_size == 0:
				raise OSError("Empty File")
			image_arr = image.imread(path)
			print(f"Loading image of dimensions {image_arr.shape[0]} x {image_arr.shape[1]}")
			return (image_arr)
		except FileNotFoundError or OSError as err:
			print(err.args)

	@staticmethod
	def display(array):
		try:
			if not isinstance(array, np.ndarray):
				raise ValueError("Input is of WrongType")
			pyplot.imshow(array)
			pyplot.show()
		except ValueError as err:
			print(err.args)
