#!/usr/bin/python

import sys

divisible_without_remainder = lambda a, b: a % b == 0

def try_divisables(n, d):
  if d == 21:
    print n
    sys.exit()
  elif not divisible_without_remainder(n, d):
    return
  else:
    if divisible_without_remainder(n, d):
      try_divisables(n, d + 1)

for i in xrange(10000, 500000000):
  try_divisables(i, 1)
