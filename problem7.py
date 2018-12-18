#!/usr/bin/python

def is_prime(n):
  if n == 2:
    return True
  for i in range(2, n):
    if not n % i:
      return False
  return True

primes = []

for n in xrange(2, 200000):
  if len(primes) == 10001:
    break
  else:
    if is_prime(n):
      primes.append(n)

print primes[-1]
