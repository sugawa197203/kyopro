# N, Q = map(int, input().split())
# S = input()

N = 5 * 10**5
Q = 5 * 10**5
S = "1" * N

FLAG = [0] * (N - 1)

_s = S[0]
for i, s in enumerate(S[1:]):
	if _s != s:
		FLAG[i] = 1
	_s = s

OUTPUT = []

for i in range(Q):
	#q, L, R = input().split()
	q, L, R = "2", "1", str(N)
	L, R = int(L), int(R)
	#print(f"q:{q}, L:{L}, R:{R} FLAG:{FLAG}")
	if q == "1":
		if L != 1:
			if FLAG[L - 2] == 1:
				FLAG[L - 2] = 0
			else:
				FLAG[L - 2] = 1
		if R != N:
			if FLAG[R-1] == 1:
				FLAG[R-1] = 0
			else:
				FLAG[R-1] = 1
	else:
		_f = False
		for f in FLAG[L - 1:R - 1]:
			if f == 1:
				continue
			else:
				_f = True
				OUTPUT.append("No")
				break
		if not _f:
			OUTPUT.append("Yes")

print("\n".join(OUTPUT))
