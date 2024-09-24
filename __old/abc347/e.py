N, Q = map(int, input().split())
x = list(map(int, input().split()))

S:set[int] = set()
Slen = 0
A = [0] * N

for _x in x:
	if _x in S:
		Slen -= 1
		S.remove(_x)
		for s in S:
			A[s - 1] += Slen
	else:
		Slen += 1
		S.add(_x)
		for s in S:
			A[s - 1] += Slen

print(" ".join(map(str, A)))