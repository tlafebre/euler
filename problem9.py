#!/usr/bin/python

import sys

def is_ascending_triplet(a, b, c):
  return True if a < b < c else False

def is_pythagorean(a, b, c):
  return True if a + b == c else False

def is_pythagorean_triplet(a, b, c):
  a, b, c = a**2, b**2, c**2 
  return True if is_ascending_triplet(a, b, c) and is_pythagorean(a, b, c) else False
  
for i, j, k in xrange(1, 1000):
  for j in xrange(1, 1000):
    for k in xrange(1, 1000):
      if is_pythagorean_triplet(i, j, k):
        if i + j + k == 1000:
          print "%d >>> pythagorean triplet: %d * %d * %d" % ((i * j * k), i, j , k)
          sys.exit()
