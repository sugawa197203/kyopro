S = list(input())
T = list(input())

TT = set(T)

for i in range(1, len(S)):
	if S[i].isupper():
		if S[i-1] not in TT:
			print("No")
			exit()
	
print("Yes")