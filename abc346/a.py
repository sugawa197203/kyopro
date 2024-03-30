N = int(input())
A = list(map(int, input().split()))

r = []

for a, b in zip(A[:-1], A[1:]):
	r.append(b * a)

print(" ".join(map(str, r)), end="")