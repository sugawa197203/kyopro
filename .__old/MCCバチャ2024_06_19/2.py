S = list(input())
T = list(input())

minimun = 999999

for start in range(len(S) - len(T) + 1):
	diff = 0
	for i in range(len(T)):
		if S[start + i] != T[i]:
			diff += 1
	minimun = min(minimun, diff)

print(minimun)