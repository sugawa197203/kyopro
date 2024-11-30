N, M = map(int, input().split())
_m = M % 10
s = [i for i in range(1, _m+1)]
t = [1] * N
ans = []

while t[0] != _m:
	ans.append([i * 10 + _t for i, _t in enumerate(t)])

	if t[-1] < _m:
		t[-1] += 1
		continue

	for j in range(N):
		if t[j] != _m:
			continue

		if j == 0:
			break
		
		t[j-1] = t[j-1] + 1
		
		for k in range(j, N):
			t[k] = t[j-1]

ans.append([i * 10 + _m for i, _t in enumerate(t)])

print(len(ans))
[print(*i) for i in ans]