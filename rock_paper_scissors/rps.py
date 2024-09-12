#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  final = []
  options = [['rock'], ['paper'], ['scissors']]
  # recursive calls 'n' times over options generating all permutations
  def list_gen(n, arr=[]):
    if n == 0: return final.append(arr)
    # add options 'i' to arr 'n' times
    for i in options:
      list_gen(n-1, arr + i)
    # return final
  list_gen(n)
  return final
print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')