N, T = map(int, input().split())
A, B = [], []
for _ in range(T):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)

kind = 1
scores = [0] * N
d = dict()
d[0] = N

for i in range(T):
	a = A[i]
	b = B[i]
	Ascore = scores[a-1]
	d[Ascore] = d.get(Ascore) - 1
	if d.get(Ascore) == 0:
		del d[Ascore]
		kind -= 1
	Ascore += b
	scores[a-1] = Ascore
	d[Ascore] = d.get(Ascore, 0) + 1
	if d.get(Ascore) == 1:
		kind += 1
	print(kind)
	