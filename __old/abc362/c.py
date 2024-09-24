def clamp(x, l, r):
	return min(r, max(l, x))

N = int(input())
L, R = [0]*N, [0]*N

for i in range(N):
	L[i], R[i] = map(int, input().split())

sumL, sumR = sum(L), sum(R)

if not(sumL <= 0 and 0 <= sumR):
	print("No")
	exit()

ans = [0]*N
vle = 0

print("Yes")

for i, (l, r) in enumerate(zip(L, R)):
	sumL -= l
	sumR -= r
	ans[i] = clamp(-(sumL + sumR + vle + vle)//2, l, r)
	vle += ans[i]

print(*ans)
