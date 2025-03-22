N = int(input())

ans = None

if N % 2 == 0:
	ans = ["-" for i in range(N)]
	ans[N // 2] = "="
	ans[N // 2 - 1] = "="
else:
	ans = ["-" for i in range(N)]
	ans[N // 2] = "="

print("".join(ans))
