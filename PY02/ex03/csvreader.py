import os

class CsvReader():

	def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
		try:
			if not filename:
				raise ValueError("Cannot initialize CsvReader without a file")
			for root, direc, files in os.walk("."):
				if filename not in files:
					raise ValueError("File not found")
			self.filename = filename
			self.sep = sep
			self.header = header
			if (skip_top < 0 or skip_bottom < 0):
				raise ValueError("Header skipping values cannot be negatives")
			self.skip_top = skip_top
			self.skip_bottom = skip_bottom
		except OSError and ValueError as err:
			print(err.args)
	
	def __enter__(self):
		self.fd = open(self.filename, 'r')
		self.nb_columns = len(self.fd.readline().split(self.sep))
		print(self.nb_columns)
		return self

	def __exit__(self):
		self.fd.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom. 
		Returns: nested list (list(list, list, ...)) representing the data."""


	def getheader(self):
		""" Retrieves the header from csv file. Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
