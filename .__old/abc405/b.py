N, M = map(int, input().split())
A = list(map(int, input().split()))

target = list(range(1, M + 1))

ans = 0

for i in range(N + 1):
	for t in target:
		if t not in A:
			print(ans)
			exit()
	
	ans += 1
	A.pop()

print(ans)
