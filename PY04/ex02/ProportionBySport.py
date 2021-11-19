from FileLoader import FileLoader

def proportionBySport(data, year, sport, gender):
	sub_frame = data[(data["Year"] == year) & (data["Sport"] == sport) & (data["Sex"] == gender)]
	sub_frame_gdr = data[(data["Year"] == year) & (data["Sex"] == gender)]
	return (~sub_frame.duplicated(subset='Name')).sum() / (~sub_frame_gdr.duplicated(subset='Name')).sum()


fl = FileLoader()
data = fl.load("athlete_events.csv")
print(proportionBySport(data, 2004, "Tennis", "F"))
