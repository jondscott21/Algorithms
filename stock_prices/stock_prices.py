#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # assign min to prices[0]
  curr_max = prices[1] - prices[0]
  # assign max to prices[1]
  #  loop over 'prices' starting at index 2
  for i in range(len(prices)):
    for j in range(i):
  # assign min/max as needed making sure that min is a lesser index than max
      diff = prices[i] - prices[j]
      if diff > curr_max:
        curr_max = diff
  return curr_max
  # return max - min
print(find_max_profit([10, 7, 5, 8, 11, 9]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))