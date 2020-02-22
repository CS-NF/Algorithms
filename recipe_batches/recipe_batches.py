#!/usr/bin/python

import math

#  *** Understand *** 
# I know that the arguments recipeand ingredients are dictionaries 
#  In the ingredient dictionary the key is how much of the ingredient you in your personal inventory (What the cook as in the kitchen) 
# In the recipe dictionary the key is going to be the ingredient name and the value is how much of that ingredient the recipe requires (the ingredients that are only in the book/recipe) 
# What I need to do:  using the ingredient dictionary find the maximum number of whole batches that can be made

# *** Plan (pseudocode) ***
# create for loop


def recipe_batches(recipe, ingredients):
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))