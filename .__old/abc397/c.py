N = int(input())
A = list(map(int, input().split()))

foward = [0] * (N - 1)
backward = [0] * (N - 1)

t = [0] * (10**6+1)
count = 0
for i, a in enumerate(A[:-1]):
	if t[a] == 0:
		count += 1
		t[a] = 1

	foward[i] = count

t = [0] * (10**6+1)
count = 0
for i, a in enumerate(A[:0:-1]):
	if t[a] == 0:
		count += 1
		t[a] = 1

	backward[i] = count

print(max([f + b for f, b in zip(foward, reversed(backward))]))
