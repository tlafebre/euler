#!/usr/bin/python

def gen_primes():
  """Sieve of Eratosthenes"""
  d = {}
  n = 2
  while True:
    if n not in d:
      yield n
      d[n * n] = [n]
    else:
      for p in d[n]:
        d.setdefault(p + n, []).append(p)
      del d[n]
    n += 1

prime_sum = 0
for i in gen_primes():
  if i >= 2000000:
    break
  else:
    prime_sum += i

print prime_sum
