from itertools import combinations
from functools import reduce
def xor(__a:list)->int:return reduce(lambda __x, __y: __x ^ __y, __a) if len(__a) > 1 else 0 if len(__a) == 0 else __a[0]

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
allxor = 0
if N - K < K:
	K = N - K
	allxor = xor(A)

[ans := max(ans, allxor ^ xor(a)) for a in combinations(A, K)]
print(ans)
