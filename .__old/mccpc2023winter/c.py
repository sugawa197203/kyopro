N, D = map(int, input().split())
S = list(input())
if N != D:
	if S[0] == "0":
		for i in range(D - N):
			S.insert(0, "1")
	else:
		S.extend(["1"] * (D - N))
	print(int("".join(S)))
	
else:
	print(int("".join(S)))
