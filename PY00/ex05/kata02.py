from datetime import datetime

t = (3,30,2019,9,25)

data = datetime(t[2], t[3], t[4], t[0], t[1], 0)
data_format = data.strftime("%d/%m/%Y %H:%M")
print(data_format)
