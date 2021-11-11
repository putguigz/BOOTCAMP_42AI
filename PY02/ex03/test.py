from csvreader import CsvReader

if __name__ == "__main__":
	with CsvReader("good.csv", header=True) as file:
		data = file.getdata()
		header = file.getheader()
		print(header)