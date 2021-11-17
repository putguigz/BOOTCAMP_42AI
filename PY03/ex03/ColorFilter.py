
from ImageProcessor import ImageProcessor
import numpy as np
import copy

class ColorFilter:
	@staticmethod
	def invert(array):
		if not isinstance(array, np.ndarray) or not all(isinstance(elem, (np.ndarray, float)) for elem in array):
			return None
		else:
			return 1 - array[:, :, :3]

	@staticmethod
	def to_blue(array):
		if not isinstance(array, np.ndarray) or not all(isinstance(elem, (np.ndarray, float)) for elem in array):
			return None
		else:
			cpy = np.zeros(np.shape(array))
			cpy[:, :, 2] = array[:, :, 2]
			cpy[:, :, 3] = array[:, :, 3]
			return (cpy)

	@staticmethod
	def to_red(array):
		if not isinstance(array, np.ndarray) or not all(isinstance(elem, (np.ndarray, float)) for elem in array):
			return None
		else:
			cf = ColorFilter()
			tmp = array[:, :, :3] - cf.to_blue(array)[:, :, :3] - cf.to_green(array)[:, :, :3]
			return tmp
	
	@staticmethod
	def to_green(array):
		if not isinstance(array, np.ndarray) or not all(isinstance(elem, (np.ndarray, float)) for elem in array):
			return None
		else:
			cpy = copy.deepcopy(array)
			cpy[:, :, 0] = 0
			cpy[:, :, 2] = 0
			return (cpy)

	@staticmethod
	def to_grayscale(array, filter, **kwargs):
		if not isinstance(array, np.ndarray) or not all(isinstance(elem, (np.ndarray, float)) for elem in array):
			return None
		else:
			if filter == 'm' or filter == 'mean':
				r = 0.2989
				g = 0.5870
				b = 0.1140
			elif filter == 'w' or filter == 'weighted':
				if len(kwargs) != 3:
					return None
				else:	
					r = kwargs[0]
					g = kwargs[1]
					b = kwargs[2]
			else:
				return None
			new_array = np.dstack((array[:,:,0] * 0.2989 + array[:,:,1] * 0.5870 + array[:,:,2] * 0.1140,\
				 array[:,:,0] * 0.2989 + array[:,:,1] * 0.5870 + array[:,:,2] * 0.1140,\
					  array[:,:,0] * 0.2989 + array[:,:,1] * 0.5870 + array[:,:,2] * 0.1140,\
						   array[:,:,3]))
			return new_array
		
	@staticmethod
	def to_celluloid(array):
		pass


imp = ImageProcessor()
cf = ColorFilter()
arr = imp.load("assets/elon_canaGAN.png")

imp.display(cf.invert(arr))
imp.display(arr)
imp.display(cf.to_blue(arr))
imp.display(arr)
imp.display(cf.to_green(arr))
imp.display(arr)
imp.display(cf.to_red(arr))
imp.display(arr)
imp.display(cf.to_grayscale(arr, "m"))
imp.display(arr)

interval = np.linspace(0, 1, 5)
print(interval)