#!/usr/bin/python
 
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiple_of(n): return True if n % 3 == 0 or n % 5 == 0 else False

check    = sum([i for i in range(10) if multiple_of(i)])
solution = sum([i for i in range(10) if multiple_of(i)])

print solution
