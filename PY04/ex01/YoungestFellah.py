from FileLoader import FileLoader
import pandas as pd

def youngfellah(df, year):
	dico = {}
	dico["woman"] = dico["man"] = "NaN"
	if not isinstance(df, pd.DataFrame):
		return dico
	else:
		males = df[df['Sex'] == 'M']
		females = df[df['Sex'] == 'F']
		dico["man"] = df.loc[males["Age"].idxmin()]["Name"]
		dico["woman"] = df.loc[females["Age"].idxmin()]["Name"]
		return dico

	
fl = FileLoader()
data = fl.load("athlete_events.csv")
dico  = youngfellah(data, 1992)
print(dico)