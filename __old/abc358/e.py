import math

K = int(input())
C = list(map(int, input().split()))

ans = 0
total = sum(C)

for r in range(1, K + 1):
	allPattern = math.perm(total, r)
	chohukuPattern = 0
	for i in range(26):
		chohukuPattern += math.perm(C[i], r) - 1
		print(chohukuPattern)
	ans += allPattern - chohukuPattern
	print(allPattern, chohukuPattern)


print(ans % 998244353)