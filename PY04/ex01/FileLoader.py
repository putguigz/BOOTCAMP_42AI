import pandas as pd

class FileLoader:
	@staticmethod
	def load(path):
		'''Load file, print dimensions, return a pandas.DataFrame of datas'''
		ret = pd.read_csv(path)
		size = ret.shape
		print(f"Dimensions of the Dataset are {size[0]} rows X {size[1]} columns")
		return pd.read_csv(path)

	@staticmethod
	def display(df, n):
		if not isinstance(df, pd.DataFrame) or not isinstance(n, int):
			return 
		else:
			if n >= 0:
				print(df.head(n))
			else:
				print(df.tail(-n))

if __name__ == "__main__":
	fl = FileLoader()
	tab = fl.load("athlete_events.csv")
	fl.display(tab, 12)
