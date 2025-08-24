from sortedcontainers import SortedList

Q = int(input())

hukuro = SortedList()
for _ in range(Q):
	q = list(map(int, input().split()))
	if q[0] == 1:
		hukuro.add(q[1])
	elif q[0] == 2:
		tama = min(hukuro)
		hukuro.remove(tama)
		print(tama)
