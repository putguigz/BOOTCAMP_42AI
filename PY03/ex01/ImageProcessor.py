from PIL import Image
import numpy as np
import os

class ImageProcessor:

	@staticmethod
	def load(path):
		try:
			image = Image.open(path)
			if os.stat(path).st_size == 0:
				raise OSError("Empty File")
			print(f"Loading image of dimensions {image.size[0]} x {image.size[1]}")
			return (np.asarray(image))
		except FileNotFoundError or OSError as err:
			print(err.args)

	def display(array):
		try:
			if isinstance(array, list):
				raise ValueError("Input is of WrongType")
			img = Image.fromarray(array)
			img.show()
		except ValueError as err:
			print(err.args)


img = ImageProcessor.load("42AI.png")
print(type(img))
print(img)
ImageProcessor.display(img)