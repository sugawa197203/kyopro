N, M = map(int, input().split())
ans = 0
import math
for i in range(1, 62):
	mask = 1 << (i-1)
	if M & mask:
		q = N // (2**i)
		r = N % (2**i)
		ans += q * (2**(i-1)) + max(0, r - (2**(i-1)) + 1)

print(ans % 998244353)