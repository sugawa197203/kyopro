N = int(input())
A = list(map(int, input().split()))

import sortedcontainers
kureruninzuu = sortedcontainers.SortedList()
nokori = 0

for i in range(N):
	morau = min(len(kureruninzuu), nokori)
	ageru = min(A[i] + morau, N - i - 1)
	nokori += ageru - morau
	A[i] += morau - ageru
	kureruninzuu.add(i + ageru)
	while kureruninzuu and kureruninzuu[0] <= i:
		kureruninzuu.discard(kureruninzuu[0])
	
print(*A)
