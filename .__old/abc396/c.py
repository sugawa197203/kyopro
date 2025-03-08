N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

Bcount = 0
Wcount = 0
ans = 0

for i in range(N):
	if 0 <= B[i]:
		Bcount += 1
		ans += B[i]
	else:
		break

for i in range(M):
	if 0 <= W[i] and Wcount < Bcount:
		Wcount += 1
		ans += W[i]
	else:
		break

if M == Wcount or W[Wcount] <= 0:
	print(ans)
	exit()
	
while Bcount < N and Wcount < M and 0 <= W[Wcount] + B[Bcount]:
	ans += W[Wcount] + B[Bcount]
	Wcount += 1
	Bcount += 1

print(ans)
