N = int(input())
S = input()
C = list(map(int, input().split()))

i = 1
cost = 0

while i < N:
	if S[i] == S[i - 1]:
		cost += min(C[i - 1], C[i])
	i += 1