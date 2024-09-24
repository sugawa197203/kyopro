
def seartchbit(b):
	a = 0
	l = []
	while a <= b:
		if (1 << a) & b != 0:
			l.append(a)
		a += 1
	return l


while True:
	n = int(input())
	if n == 0:
		exit(0)
	S = input()
	
	score = 0
	points = []

	for i, s in enumerate(S):
		if s == 'o' and i != 0 and i != n:
			_n = len(points)
			bittable = 0
			stop = 2 ** _n
			
			flag = False

			manpointssum = 0

			while bittable < stop:
				l = seartchbit(bittable)
				print(l)
				pointsum = 0
				for _l in l:
					pointsum += points[_l]

				if pointsum > manpointssum:
					manpointssum = pointsum

				if pointsum == i + 1:
					flag = True
					break
				
				bittable += 1
			
			if not flag:
				if len(points) == 0:
					points.append(i)
				else:
					points.append(i - manpointssum)
	
	psum = sum(points)
	print("DEBUG", points, psum, n)
	if psum == n:
		print(len(points))
	else:
		print(len(points) + 1)

