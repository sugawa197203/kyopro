N = int(input())

A = list(map(int, input().split()))

S, T = [] , []
for i in range(N - 1):
	s, t = map(int, input().split())
	S.append(s)
	T.append(t)

for i in range(N - 1):
	v = A[i] // S[i]
	get = T[i] * v
	A[i+1] += get

print(A[-1])