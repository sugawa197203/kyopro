N, x, y = map(int, input().split())
A = list(map(int, input().split()))

yoko = []
tate = []

for i in range(N):
	if i % 2:
		tate.append(A[i])
	else:
		yoko.append(A[i])
yokosum = sum(yoko)
tatesum = sum(tate)
yokof = False
# yoko
for size in range((N+1) // 2):
	for i in range(N - size):
		length = sum(yoko[i:i+size])
		if length - yokosum == x or yokosum - length == x:
			yokof = True
			break
	if yokof:
		break

# tate