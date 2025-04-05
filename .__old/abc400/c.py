import math

N = int(input())

ans = 0
k = 1
while (1 << k) <= N:
	limit = N // (1 << k)
	M = math.isqrt(limit)
	count_odds = (M + 1) // 2
	ans += count_odds
	k += 1
	
print(ans)