import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

Aacc = [0] * (N + 1)
for i in range(N):
	Aacc[i + 1] = Aacc[i] + A[i]
	
maxA = A[-1]

def solve(b):
	if b > maxA:
		print("-1")
		return
	
	if b == 1:
		print("1")
		return

	
	idx = bisect.bisect_left(A, b)

	if idx == 0:
		print(1 + len(A) * (b - 1))
		return
	
	print(1 + Aacc[idx] + (b - 1) * (len(A) - idx))


for _ in range(Q):
	b = int(input())
	solve(b)
