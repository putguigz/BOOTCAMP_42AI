from math import sqrt
import sys
import random
from numpy.lib.shape_base import split
from csvreader import CsvReader
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class KmeansClustering:
	def __init__(self, max_iter=20, ncentroid=4):
		if not isinstance(ncentroid, int) or not isinstance(max_iter, int):
			raise ValueError("max_iter and/or ncentroid are of wrong type")
		if max_iter <= 0 or ncentroid <= 0:
			raise ValueError("Negative or equal to zero parameters")
		self.ncentroid = ncentroid
		self.max_iter = max_iter
		self.centroids = []				

	def shortest_distance_index(self, centroids, elem):
		dico = {0:[], 1:[], 2:[]}
		for i in dico:
			dico[i] = sqrt((centroids[i][0] - elem[0]) ** 2 + (centroids[i][1] - elem[1]) ** 2 + (centroids[i][2] - elem[2]) ** 2)
		return (min(dico, key=dico.get))	

	def fit(self, X):
		if not isinstance(X, np.ndarray):
			return None
		else:
			flatened = np.ndarray.flatten(X)
			a_centroids = np.ndarray((self.max_iter, 3, 3))
			for i in range(self.max_iter):
				for j in range(3):
					for x in range(3):
						a_centroids[i][j][x] = random.uniform(min(flatened), max(flatened))
			for i in range(self.max_iter):
				new_list = [[], [], []]
				for j, elem in enumerate(X):
					idx = self.shortest_distance_index(a_centroids[i], elem)
					new_list[idx].append(j)
				print(new_list)

	def predict(self, X):
		pass

def main():
	lst = sys.argv[1:]
	if len(lst) != 1 and len(lst) != 2 and len(lst) != 3:
		raise ValueError("Wrong number of arguments")
	else:
		kwlst = {"filepath" : "", "max_iter" : 20, "ncentroid": 4}
		for elem in lst:
			elem = elem.split("=")
			if elem[0] in kwlst:
				kwlst[elem[0]] = elem[1]
		with CsvReader(kwlst["filepath"]) as file:
		   data = file.getdata()
		data = np.reshape(data, (len(data), 4))
		split = data[:, 1:].astype(float)

		#ax = plt.axes(projection='3d')
		#ax.scatter3D(split[:, 0], split[:, 1], split[:, 2])
		#plt.show()

		hp = KmeansClustering(int(kwlst["max_iter"]), int(kwlst["ncentroid"]))
		hp.fit(split)

if __name__ == "__main__":
	try:
		main()
	except ValueError as err:
		print(err.args)