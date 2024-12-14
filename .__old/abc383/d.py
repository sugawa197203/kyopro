N = int(input())

import math

def eratosthenes(limit):
	isprime = [True] * (limit + 1)
	isprime[0] = isprime[1] = False
	for i in range(2, int(math.sqrt(limit)) + 1):
		if isprime[i]:
			for multiple in range(i * i, limit + 1, i):
				isprime[multiple] = False
	return [x for x in range(limit + 1) if isprime[x]]

primes = eratosthenes(int(N**(1/2)) + 1)

count = 0

for p in primes:
	if p**8 > N:
		break
	count += 1

for i in range(len(primes)):
	for j in range(i + 1, len(primes)):
		if primes[i]**2 * primes[j]**2 > N:
			break
		count += 1
	
print(count)