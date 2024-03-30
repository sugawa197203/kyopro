N, Q = map(int, input().split())
query = [tuple(input().split()) for _ in range(Q)]
heads = [(x, 0) for x in range(N, 0, -1)]
i = N
for q in query:
	if q[0] == '1':
		if q[1] == 'R':
			heads.append((heads[i - 1][0] + 1, heads[i - 1][1]))
		elif q[1] == 'L':
			heads.append((heads[i - 1][0] - 1, heads[i - 1][1]))
		elif q[1] == 'U':
			heads.append((heads[i - 1][0], heads[i - 1][1] + 1))
		elif q[1] == 'D':
			heads.append((heads[i - 1][0], heads[i - 1][1] - 1))
		i += 1
	else:
		h = heads[i - int(q[1])]
		print(h[0], h[1])
