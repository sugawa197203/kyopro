
while True:
	d = dict()
	n = int(input())
	if n == 0:
		exit(0)
	
	a = list(map(int, input().split(' ')))

	for i, _n in enumerate(a):
		d[i] = _n
	
	nearid = -1
	neardistance = 210000000

	for k, v in d.items():
		if neardistance > abs(v - 2023):
			nearid = k
			neardistance = abs(v - 2023)
		
	print(nearid + 1)
