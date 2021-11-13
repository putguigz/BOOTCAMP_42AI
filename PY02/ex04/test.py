import my_minipack.logger

from time import sleep

listy = range(1000)
ret = 0
for elem in progressbar(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)
