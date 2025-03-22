N = int(input())
A = list(map(int, input().split()))

from collections import Counter

c = Counter(A)

num = -1

for k, v in c.items():
	if v == 1:
		num = max(num, k)
if num == -1:
	print("-1")
else:
	print(A.index(num) + 1)
