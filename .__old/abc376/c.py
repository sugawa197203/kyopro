N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)

import sys
debug = lambda *args: print(*args, file=sys.stderr)

debug(A)
debug(B)

ans = -1
idx = 0
for a in A:
	if a <= B[idx]:
		idx += 1
		if idx == len(B):
			if ans == -1:
				ans = A[-1]
			break
	else:
		if ans == -1:
			ans = a
			continue
		print(-1)
		exit(0)

print(ans)
