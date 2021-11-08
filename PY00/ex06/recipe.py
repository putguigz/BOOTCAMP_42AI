cookbook = {
        "sandwich" : {'ingredients' : ['ham', 'bread', 'cheese'], 'meal' : 'lunch', 'prep_time' : 10},
        "cake" : {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60},
        "salad" : {'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal' : 'lunch', 'prep_time' : 15}
}

def print_recipe(name):
    if name in cookbook:
        print("Ingredients list:", cookbook[name]["ingredients"])
        print("To be eaten for", cookbook[name]["meal"], end=".\n")
        print("Takes", cookbook[name]["prep_time"], "of cooking.\n")

def delete_recipe(name):
    if name in cookbook:
        del cookbook["sandwich"]

def add_recipe(name, ingredients, meal, prep_time):
    if name in cookbook:
        return
    else:
        cookbook[name] = {'ingredients' : ingredients, 'meal' : meal, 'prep_time' : prep_time}

def list_recipes():
    print("\n{0:-^42}".format('RECIPES'))
    for key in cookbook:
        print("{0:.>42}".format(key))
    print()

while 1:
    answer = input("Please select an option by typing the corresponding number:\n\
    1: Add a recipe\n\
    2: Delete a recipe\n\
    3: Print a recipe\n\
    4: Print the cookbook\n\
    5: Quit\n")
    
    if answer == "1":
        recipe_name = input("Enter Recipe Name:\n")
        ingredients_needed = input("Enter list of ingredients, separated by spaces:\n").split()
        meal = input("Enter a Meal Type:\n")
        prep_time = input("Time needed to cook that recipe:\n")
        add_recipe(recipe_name, ingredients_needed, meal, prep_time)
    elif answer == '2':
        recipe_name = input("Enter name of recipe you wish to delete:\n")
        delete_recipe(recipe_name)
    elif answer == '3':
        recipe_name = input("Enter name of recipe you wish to display:\n")
        print_recipe(recipe_name)
    elif answer == '4':
        list_recipes()
    elif answer == '5':
        print("Cookbook closed.")
        quit()
    else:
        continue
