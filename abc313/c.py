N = int(input())
import math
A = list(map(float, input().split(" ")))

if N == 1:
	print(0)
	exit()

avg = float(sum(A)) / float(len(A))
avg = round(avg, 0)

ma = max(A)
mi = min(A)

avgfloor = float(math.floor(avg))
avgceil = float(math.ceil(avg))

count = 0.0
for i in range(N):
	if A[i] < avg:
		count += avgfloor - A[i]
	else:
		count += A[i] - avgceil
		
print(math.ceil(count / 2) - 1)
