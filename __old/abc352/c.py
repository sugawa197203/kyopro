N = int(input())
A, B = [], []
maximizeHead = 0
for i in range(N):
	a, b = map(int, input().split())
	A.append(a)
	B.append(b)
	maximizeHead = max(maximizeHead, b - a)

print(sum(A) + maximizeHead)
