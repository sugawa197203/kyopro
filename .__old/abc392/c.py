N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

humanByZekken = [0] * N
ZekkenByHuman = [0] * N
LookByHuman = [0] * N
humanByLook = [0] * N
for i in range(N):
	ZekkenByHuman[i] = Q[i] - 1
	LookByHuman[i] = P[i] - 1
	humanByZekken[Q[i] - 1] = i
	humanByLook[P[i] - 1] = i

ans = []
for i in range(N):
	human = humanByZekken[i]
	lookingAt = LookByHuman[human]
	zekken = ZekkenByHuman[lookingAt]
	# print(human, lookingAt, zekken)
	ans.append(zekken + 1)

print(*ans)