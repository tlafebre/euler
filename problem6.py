#!/usr/bin/python

def sum_of_squares_up_until(n):
  sum_of_squares = 0
  for i in range(1, n + 1):
    sum_of_squares += i**2
  return sum_of_squares

def square_of_sum_up_until(n):
  sum_up_until = 0
  for i in range(1, n + 1):
    sum_up_until += i
  return sum_up_until**2

n = 100

print square_of_sum_up_until(n) - sum_of_squares_up_until(n)
