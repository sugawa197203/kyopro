S = list(input())

for i in range(len(S) - 1, 0, -1):
	if S[i] == "A" and S[i - 1] == "W":
		S[i] = "C"
		S[i - 1] = "A"

print("".join(S))		
