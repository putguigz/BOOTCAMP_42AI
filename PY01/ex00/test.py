
from recipe import Recipe
from book import Book

houmous = Recipe("Houmous", 3, 10, ["pois-chiche", "huile de sesame"], "Tres Bon", "starter")
chawarma = Recipe("Chawarma", 1, 20, ["poulet", "citron", "Tahina"], "", "lunch")
mouhalabiheh = Recipe("Mouhalabiheh", 5, 60, ["eau de rose", "lait", "maizena"], "", "dessert")
fondant = Recipe("Fondant", 2, 40, ["Chocolat noir", "farine"], "Delicieux", "dessert")


book = Book("Jamie Oliver's Cooking Book")
book.add_recipe(houmous)
book.add_recipe(chawarma)
book.add_recipe(mouhalabiheh)
book.add_recipe(fondant)
book.get_recipes_by_types("dessert")
book.get_recipe_by_name("Houmous")