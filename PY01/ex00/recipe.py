
def	check_confo_class(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
	if type(name) != str:
		print("Wrong Format: name")
		quit()
	elif not name:
		print("Empty string: name")
		quit()
	if type(cooking_lvl) != int:
		print("Wrong Format: cooking_lvl")
		quit()
	elif cooking_lvl < 1 or cooking_lvl > 5:
		print("Not in Range: cooking_lvl")
		quit()
	if type(cooking_time) != int:
		print("Wrong Format: cooking_time")
		quit()
	elif cooking_time < 0:
		print("Negative Number: cooking_time")
		quit()
	if type(ingredients) != list:
		print("Wrong Format: ingredients")
		quit()
	elif not ingredients:
		print("Empty list of ingredients")
		quit()
	else:
		for elem in ingredients:
			if type(elem) != str:
				print("Wrong Format: element in ingredients")
				quit()
			elif not elem:
				print("Empty string: element in ingredients")
				quit()
	if type(description) != str:
		print("Wrong Format: description")
		quit()
	if type(recipe_type) != str:
		print("Wrong Format: recipe_type")
		quit()
	elif not recipe_type:
		print("Empty string: recipe_type")
		quit()
	elif recipe_type not in ["starter", "lunch", "dessert"]:
		print("Wrong recipe_type: starter, lunch or dessert are the only options")
		quit()

class Recipe:
	def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
		check_confo_class(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
		self.name = name
		self.cooking_lvl = cooking_lvl
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.desciption = description
		self.recipe_type = recipe_type
	
	def __str__(self):
		"""Return the string to print with the recipe info"""
		return ("Recipe : " + self.name + "\nCooking Level Required : " + str(self.cooking_lvl) + "\nCooking Time : " + str(self.cooking_time) + "\nList of ingredients : " + str(self.ingredients) + "\nDescrition : " + self.desciption + "\nRecipe Type : " + self.recipe_type)
