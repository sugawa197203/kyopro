def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def reduce(p, q):
    common = gcd(p, q)
    return (p // common, q // common)

import math

T = int(input())
for c in range(T):
	N, M = map(int, input().split())
	x = math.ceil(N / M)
	a, b = reduce(x, N)
	print(a, b)
