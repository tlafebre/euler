#!/usr/bin/python

def is_palindromic(n):
  number_as_digits = list(str(n))
  return True if number_as_digits == number_as_digits[::-1] else False

palindromes = []

for a in range(1000, 100, -1):
  for b in range(1000, 100, -1):
    product = a * b
    if is_palindromic(product):
      palindromes.append(product)

print max(palindromes)
