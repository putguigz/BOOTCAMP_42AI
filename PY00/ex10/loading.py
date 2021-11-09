from time import sleep
import sys

def ft_progress(listy):
	'''RETURN POSITION IN RANGE'''	
	for i in listy:
		yield i

time_elapsed = 0
sleep_value = 0.01
range_size = 1000
remaining_range = range_size

listy = range(range_size)
ret = 0
for elem in ft_progress(listy):
	time_elapsed += sleep_value
	remaining_range-=1
	percent = (range_size - remaining_range) * 100 / range_size
	ETA = float(sleep_value * remaining_range)
	print("ETA: %.2fs [ %d%%]" % (ETA, percent), "%i/%i | " % (range_size - remaining_range, range_size), "elapsed time %.2fs" % time_elapsed, end='\r')
	
	
	ret += (elem + 3) % 5
	sleep(sleep_value)
print()
print(ret)