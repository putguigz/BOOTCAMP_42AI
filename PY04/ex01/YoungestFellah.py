from FileLoader import FileLoader
import pandas as pd

def youngfellah(df, year):
	dico = {}
	dico["woman"] = dico["man"] = "NaN"
	if not isinstance(df, pd.DataFrame):
		return dico
	else:
		males = df[(df["Year"] == year) & (df['Sex'] == 'M')]
		females = df[(df["Year"] == year) & (df['Sex'] == 'F')]
		if not males.empty:
			dico["man"] = df.loc[males["Age"].idxmin()]["Age"]
		if not females.empty:
			dico["woman"] = df.loc[females["Age"].idxmin()]["Age"]
		return dico

	
fl = FileLoader()
data = fl.load("athlete_events.csv")
dico  = youngfellah(data, 1992)
print(dico)