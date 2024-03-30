N, K = map(int, input().split())
A = list(map(int, input().split()))

costlist = []

a0 = A[0]

for a in A[1:]:
	costlist.append(a - a0)
	a0 = a

costlist2 = []

for i in range(1, len(costlist) - 1):
	costlist2.append((costlist[i - 1] + costlist[i] + costlist[i + 1], i - 1, i, i + 1))

costlist2.sort(reverse=True, key=lambda x: x[0])

