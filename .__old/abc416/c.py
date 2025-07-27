from itertools import product

N, K, X = map(int, input().split())
S = [input() for _ in range(N)]
ans = []
for i in product(range(N), repeat=K):
	s = ""
	for j in i:
		s += S[j]
	ans.append(s)

print(sorted(ans)[X-1])

