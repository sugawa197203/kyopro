S = list(input())
Q = int(input())
K = list(map(int, input().split()))
ans = []
def A010060(n):
	return n.bit_count()&1
for k in K:
	_k = A010060((k-1) // len(S))
	_k1 = k % len(S)
	if _k == 0:
		ans.append(S[_k1 - 1])
	else:
		ans.append(S[_k1 - 1].swapcase())

print(*ans)
