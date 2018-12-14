#!/usr/bin/python

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

test_number = 600851475143 

def is_prime(n):
  if n == 2:
    return True
  for i in range(2, n):
    if not n % i:
      return False
  return True

primes        = (n for n in range(2,10000) if is_prime(n))
prime_factors = [p for p in primes if test_number % p == 0]

if test_number == reduce(lambda a, b: a * b, prime_factors):
  print prime_factors[-1]
