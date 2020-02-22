#!/usr/bin/python

import argparse

#  *** Understand *** 
# The argument prices is ==  to a list of low and high pricess
# The whole idea behind this bot is to return the max profit of every buy and sell the bot makes


# *** Plan (pseudocode) ***
# create a variable called min_price and set equal to None
# create a variable called max_price and set equal to 0
# create a variable called max_profit and make equal to an empty list 
# create a for loop getting the len() of our argument price starting at the index of 0 
# if the argument price is 0 then our max price is going to be 0




def find_max_profit(prices):
  
  min_price = None 
  max_price = 0
  max_profit = []  

  for i in range(0, len(prices)):
    if prices[0] == max_price:
      max_price = prices[1]
      min_price = max_price
      max_profit = prices[:i] # start at the beginning of list until hits index
    elif prices[i] > max_price:
      max_price = prices[i]
      min_price = max_price
      max_profit = prices[:i]


  for j in range(0, len(max_profit)):
    if max_profit[j] < min_price:
      min_price = max_profit[j]
    elif max_profit[j] == max_profit[0]:
      min_price = max_profit[j]

  return max_price - min_price 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))