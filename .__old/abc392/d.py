N = int(input())
A = []
K = []
from collections import defaultdict, Counter
for i in range(N):
	k, *a = map(int, input().split())
	K.append(k)
	a = Counter(a)
	for j in a.keys():
		a[j] /= k
	A.append(a)

maxonaji = 0.0

for i in range(N):
	saikoroI = A[i]
	for j in range(i+1, N):
		saikoroJ = A[j]
		same = 0
		for k in saikoroI.keys():
			if k in saikoroJ:
				same += saikoroI[k] * saikoroJ[k]
		
		maxonaji = max(maxonaji, same)

print(maxonaji)