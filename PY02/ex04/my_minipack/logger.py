import time
import os

def logger(fct):
	fct_name = "{: <19}".format(fct.__name__.replace("_", " ").title())
	USER = os.getenv("USER")
	def new_fct(elem, water_lvl=None):
		file_log = open("machine.log", "a")
		start_chron = time.time()
		if not water_lvl:
			ret = fct(elem)
		else:
			ret = fct(elem, water_lvl)
		end_chron = time.time() - start_chron
		print(f'({USER})Running: {fct_name}', end = '', file=file_log)
		if end_chron < 1:
			print(f'[ exec_time = {end_chron * 1000:0.3f}' + ' ms' + ']', file=file_log)
		else:
			print(f'[ exec_time = {end_chron:0.3f}' + ' s' + ']', file=file_log)
		file_log.close()
		return ret
	return new_fct