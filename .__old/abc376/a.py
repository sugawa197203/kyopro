N, C = map(int, input().split())
T = list(map(int, input().split()))

last = T[0]
ans = 1
for t in T[1::]:
	if t - last < C:
		continue
	ans += 1
	last = t

print(ans)