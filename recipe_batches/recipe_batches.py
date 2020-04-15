#!/usr/bin/python

import math

'''
Spec:
  -you will be given 2 dictionaries 
  -1st is the recipe
  -2nd is the ingredients you have 
  -how many batches can you make?

first: see if you have all required ingredients 
next: see if you have _enough_ of them 
last: how many batches? 

loop through recipe
'''


def recipe_batches(recipe, ingredients):
    amounts = []

    for i in recipe:
        if i not in ingredients.keys():
            return 0
        elif recipe[i] > ingredients[i]:
            return 0
        else:
            amounts.append(ingredients[i]//recipe[i])

    return min(amounts)


recipe_batches({'milk': 2, 'sugar': 40, 'butter': 20}, {
    'milk': 5, 'sugar': 120, 'butter': 500})


# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
