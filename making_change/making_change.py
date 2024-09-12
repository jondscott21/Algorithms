#!/usr/bin/python

import sys

def making_change(amount, denominations=[1, 5, 10, 25, 50], cache={'count': 0, 'cur': 0}):
  if amount < 0: return 0
  if amount == 0: return 1
  cache['count'] = 0
  for i in range(cache['cur'], len(denominations)):
    # if not 'count' in cache:
    cache['cur'] = i
    cache['count'] += making_change(amount-denominations[i])
  return cache['count']


print(making_change(100))
# if __name__ == "__main__":
#   # Test our your implementation from the command line
#   # with `python making_change.py [amount]` with different amounts
#   if len(sys.argv) > 1:
#     denominations = [1, 5, 10, 25, 50]
#     amount = int(sys.argv[1])
#     print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
#   else:
#     print("Usage: making_change.py [amount]")