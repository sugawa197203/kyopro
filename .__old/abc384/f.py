from collections import Counter
from math import gcd

N = int(input())
A = list(map(int, input().split()))

def f(x):
    return x // (x & -x)

_A = [f(a) for a in A]
count = Counter(_A)

ans = 0

keys = list(count.keys())

for i in range(len(keys)):
	for j in range(i, len(keys)):
		if i == j:
			ans += count[keys[i]] * (count[keys[i]] - 1) // 2 * f(2 * keys[i])
		else:
			ans += count[keys[i]] * count[keys[j]] * f(keys[i] + keys[j])

print(ans)