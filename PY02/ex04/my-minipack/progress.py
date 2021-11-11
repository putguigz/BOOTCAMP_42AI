from time import *

def progressbar(listy):
	'''RETURN POSITION IN RANGE'''
	
	time_elapsed = 0
	sleep_value = 0.01
	range_size = len(listy)
	remaining_range = range_size
	for i in listy:
		start = time()
		time_elapsed += sleep_value
		remaining_range-=1
		percent = (range_size - remaining_range) * 100 / range_size
		ETA = float(sleep_value * remaining_range)
		size_loading_bar = 50
		size_stars = int(percent * size_loading_bar / 100)
		size_spaces = int(size_loading_bar - size_stars)
		sequence = "{:" + '*' + "<" + str(size_stars) + "}"
		sequence2 = "{: <" + str(size_spaces) + "}"
		progress_bar = sequence.format("") + sequence2.format("")
		print("ETA: %.2fs [ %.2d%%]" % (ETA, percent), "%s/%i |" % ("{: >4}".format(range_size - remaining_range), range_size), "[" + progress_bar + "]", "elapsed_time %.2fs" % time_elapsed, end='\r')
		yield i
		end = time() - start