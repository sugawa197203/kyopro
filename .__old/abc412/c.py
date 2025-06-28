from bisect import bisect_left, bisect_right
T = int(input())

for _ in range(T):
	N = int(input())
	S = list(map(int, input().split()))
	S = [S[0]] + sorted(list(set(S[1:-1]))) + [S[-1]]
	ans = 2

	now = S[0]
	while True:
		if S[-1] <= 2 * now:
			print(ans)
			break

		idx = bisect_right(S, 2 * now)

		if S[idx - 1] == now:
			print("-1")
			break

		if S[idx - 1] <= 2 * now:
			now = S[idx - 1]
			ans += 1
			continue

		print("-1")
		break



