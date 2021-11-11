import os

class CsvReader():

	def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
		try:
			if not filename:
				raise ValueError("Cannot initialize CsvReader without a file")
			for root, direc, files in os.walk("."):
				if root == '.':
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
		if not hasattr(self, "filename"):
			raise ValueError("filename is not set")
		self.fd = open(self.filename, 'r')

		i = self.fd.readline()
		while i == '\n':
			i = self.fd.readline()
		if i:
			self.nb_columns = len(i.split(self.sep))
		for line in self.fd.readlines():
			splited_line = line.split(self.sep)
			if len(splited_line) != self.nb_columns:# or "\n" in splited_line or None in splited_line or "" in splited_line:
				return None
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		self.fd.close()

	def getdata(self):
		""" Retrieves the data/records from skip_top to skip bottom. 
		Returns: nested list (list(list, list, ...)) representing the data."""
		
		self.fd.seek(0)
		data_list = []
		i = self.fd.readline()
		while i == '\n':
			i = self.fd.readline()
		for line in self.fd.readlines():
			mini_list = []
			for splited in line.split(self.sep):
				mini_list.append(splited.strip(" \'\"\n"))
			data_list.append(mini_list)
		return data_list


	def getheader(self):
		""" Retrieves the header from csv file. Returns:
			list: representing the data (when self.header is True).
			None: (when self.header is False).
		"""
		self.fd.seek(0)
		if not self.header:
			return None
		else:
			i = self.fd.readline()
			while i == '\n':
				i = self.fd.readline()
			list_header = []
			for splited in i.split(self.sep):
				list_header.append(splited.strip(" \'\"\n"))
			return list_header