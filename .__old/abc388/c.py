N = int(input())
A = list(map(int, input().split()))

ans = 0
import bisect
for k in A:
	ind = bisect.bisect_left(A, k*2)
	ans += N - ind
print(ans)
