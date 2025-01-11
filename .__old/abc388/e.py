N = int(input())
A = list(map(int, input().split()))

i, j = 0, N // 2
ans = 0

while i < N // 2 and j < N:
	if 2 * A[i] <= A[j]:
		print(i, j)
		ans += 1
		i += 1
		j += 1
	else:
		j += 1


print(ans)
