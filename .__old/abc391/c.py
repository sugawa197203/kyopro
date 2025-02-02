N, Q = map(int, input().split())

hukusuu = {}
homeCount = [1] * N
hatoPos = list(range(N))

for i in range(Q):
	q = list(map(int, input().split()))
	if q[0] == 1:
		p, h = q[1]-1, q[2]-1
		oldpos = hatoPos[p]
		homeCount[oldpos] -= 1
		hatoPos[p] = h
		homeCount[h] += 1
		
		if homeCount[oldpos] <= 1 and oldpos in hukusuu:
			del hukusuu[oldpos]
		if homeCount[h] > 1 and not h in hukusuu:
			hukusuu[h] = 1
	else:
		print(len(hukusuu))
