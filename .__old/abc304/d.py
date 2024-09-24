W, H = map(int, input().split(" "))
N = int(input())
P, Q = [], []

for i in range(N):
	p, q = map(int, input().split(" "))
	P.append(p)
	Q.append(q)

A = int(input())
a = list(map(int, input().split(" ")))
B = int(input())
b = list(map(int, input().split(" ")))

ichigo = dict()

for x, y in zip(P, Q):
	flag = False
	px = 0
	py = 0

	for i in range(A):
		print(";", A ,x , a[i])
		if x <= a[i]:
			px = i
			flag = True
			break

	if not flag:
		px = A
	
	flag = False
	

	for j in range(B):
		if y <= b[j]:
			py = i
			break
	
	if not flag:
		py = B


	ichigo[(px, py)] = ichigo.get((px, py), 0) + 1

saidai = max(ichigo.items(), key=lambda x: x[1])
saisyo = 0


if len(ichigo) == (A + 1) * (B + 1):
	saisyo = min(ichigo.items(), key=lambda x: x[1])[1]

print(ichigo)
print(f"{saisyo} {saidai[1]}")
