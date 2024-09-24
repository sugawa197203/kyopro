N = int(input())
D = dict()
for i in range(N):
	s, c = input().split()
	c = int(c)
	D[s] = c

_D = sorted(D.items(), key=lambda x: x[0])
total = sum(D.values())
indexN = total % N
print(_D[indexN][0])