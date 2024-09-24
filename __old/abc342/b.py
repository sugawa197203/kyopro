N = int(input())
P = list(map(int, input().split()))
Q = int(input())

for i in range(Q):
	a, b = map(int, input().split())
	aindex = P.index(a)
	bindex = P.index(b)
	if aindex < bindex:
		print(a)
	else:
		print(b)