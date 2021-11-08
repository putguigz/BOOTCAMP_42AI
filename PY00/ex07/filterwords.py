import sys
import re

if len(sys.argv) != 3 or not sys.argv[2].isdigit():
    print("ERROR")
    quit()

nb = int(sys.argv[2])
tab = re.split("\s", sys.argv[1])
filtered = []

for x in tab:
	if not len(x) <= nb:
		filtered.append(x)

print(filtered)
