N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

if M == 1:
	print(0)
	exit()

from collections import defaultdict
samekakudo = defaultdict(int)

for a, b in AB:
	samekakudo[(a + b) % N] += 1
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

samesum = sum([cmb(v, 2) for v in samekakudo.values() if v > 1])
print(cmb(M, 2) - samesum)
