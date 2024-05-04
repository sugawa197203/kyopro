import bisect
N, K = map(int, input().split())
P = list(map(int, input().split()))

if K == 1:
	print(0)
	exit()

indeices = list(range(N))
indeices.sort(key=lambda i: P[i])

print(indeices)
sizes = [0]

for i in range(1, K):
	if indeices[i] <= indeices[i-1]:
		sizes.append(sizes[i-1])
	else:
		sizes.append(indeices[i] - indeices[i-1] + sizes[i-1])
minsize = 0

for i in range(K, N):
	if indeices[i] <= indeices[i-1]:
		sizes.append(sizes[i-1] - sizes[i-K])
	else:
		sizes.append(indeices[i] - indeices[i-1] + sizes[i-1])

print(sizes)
print(minsize)
