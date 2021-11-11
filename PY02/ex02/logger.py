import time
from random import randint 
import os
from functools import wraps


def log(fct):
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


class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
			return False

	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.1)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level): 
		time.sleep(randint(1, 5))
		self.water_level += water_level
		print("Blub blub blub...")

if __name__ == "__main__":
	
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()
	
	machine.make_coffee()
	machine.add_water(70)
