Q = int(input())

que = []

for _ in range(Q):
	query = list(map(int, input().split()))
	if query[0] == 1:
		que.append(query[1])
	elif query[0] == 2:
		print(que.pop(0))