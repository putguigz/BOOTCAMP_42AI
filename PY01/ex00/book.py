import datetime

from PY01.ex00.recipe import Recipe

def check_confo_book(name, last_update, creation_date, recipes_list):
	if (type(name) != str):
		print("Wrong Format: name")
		quit()
	if (type(last_update) != datetime):
		print("Wrong Format: last_update")
		quit()
	if (type(creation_date) != datetime):
		print("Wrong Format: creation_date")
		quit()
	if (type(recipes_list) != dict):
		print("Wrong Format: recipes_list")
		quit()
	elif recipes_list not in ["starter", "lunch", "dessert"]:
		print("Recipe list not available")
		quit()
		

class Book:
	def __init__(self, name, last_update, creation_date, recipes_list):
		check_confo_book(name, last_update, creation_date, recipes_list)
		self.name = name
		self.last_update = last_update
		self.creation_date = creation_date
		self.recipes_list = recipes_list
	
	def get_recipe_by_name(self, name):
		for elem in self.recipes_list:
			if elem == name:
				print(str(self.recipes_list[name]))
				return
	
	def get_recipes_by_types(self, recipe_type):
		if recipe_type not in ["starter", "lunch", "dessert"]:
			print("Type not in Book")
			return
		print(self.recipes_list[recipe_type])
	
	def add_recipe(self, recipe):
		if type(recipe) != Recipe:
			print("Added recipe is not of Recipe type.")
			return
		self.recipes_list[recipe.recipe_type] = recipe