#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # takes two dictionary inputs
  batches = []
  # loop through the recipe dictionary and determine how many batches can me made
  for k in recipe:
  # store the rounded down values in created array, find the min value and return it
    try:
      batches.append(ingredients[k] // recipe[k])
    except:
      batches.append(0)
  return min(batches)

recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
recipe_batches(recipe, ingredients)

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))