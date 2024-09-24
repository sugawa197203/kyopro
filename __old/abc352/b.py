S = list(input())
T = list(input())

index = 0
for i, t in enumerate(T):
	if S[index] == t:
		print(i+1, end=" ")
		index += 1