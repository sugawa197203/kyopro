def OK():
	print("OK")

def NG():
	print("NG")

def serch(n, m, p, q, x):
	for i in range(m):
		if x[i] == p - 1:
			p -= 1
		elif x[i] == p:
			p += 1
	
	return p == q

while True:
	n, m, p, q = map(int, input().split(' '))
	
	if n == 0:
		exit(0)

	
	x = list(map(int, input().split(' ')))
	
	if serch(n, m, p, q, x):
		OK()
		continue

	flag = False
	for _m in range(m + 1):
		for _n in range(n - 1):
			_x = x.copy()
			_x.insert(_m, _n + 1)

			if serch(n, m + 1, p, q, _x):
				print(_n + 1, _m)
				flag = True
				break
		if flag:
			break
	if flag:
		continue

	NG()
