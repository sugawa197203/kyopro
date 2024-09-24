N = int(input())
L = []
A = set()

for i in range(N):
	l, *a = map(int, input().split())
	L.append(l)
	A.add(tuple(a))

print(len(A))
