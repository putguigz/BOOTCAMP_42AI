from csvreader import CsvReader

if __name__ == "__main__":
	with CsvReader("good.csv") as file:
		data = file.getdata()
		for elem in data:
			print(elem)
		header = file.getheader()
		print(header)