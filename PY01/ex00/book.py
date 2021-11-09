from datetime import datetime
from recipe import Recipe

def check_confo_book(name):
	if (type(name) != str):
		print("Wrong Format: name")
		quit()
	#if (type(recipes_list) != dict):
	#	print("Wrong Format: recipes_list")
	#	quit()
	#elif recipes_list not in ["starter", "lunch", "dessert"]:
	#	print("Recipe list not available")
	#	quit()
		

class Book:
	def __init__(self, name):
		check_confo_book(name)
		self.name = name
		self.last_update = 0
		self.creation_date = datetime.today()
		self.recipes_list = {"starter" : [], "lunch" : [], "dessert" : []}
	
	def get_recipe_by_name(self, name):
		for key, value in self.recipes_list.items():
			for elem in value:
				if name == elem.name:
					print(elem)
				return
	
	def get_recipes_by_types(self, recipe_type):
		if recipe_type not in ["starter", "lunch", "dessert"]:
			print("Type not in Book")
			return
		for elem in self.recipes_list[recipe_type]:
			print(elem, end="\n\n")
	
	def add_recipe(self, recipe):
		if type(recipe) != Recipe:
			print("Added recipe is not of Recipe type.")
			return
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update = datetime.now()