N, M = map(int, input().split())
A = set(map(int, input().split()))

ans = []
for n in range(1, N+1):
	if n not in A:
		ans.append(n)

print(len(ans))
if len(ans) == 0:
	print()
else:
	print(*ans)