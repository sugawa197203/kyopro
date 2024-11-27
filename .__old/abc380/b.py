S = input()
S = S[1::]
S = S[:-1]

s = S.split("|")
A = []
for _s in s:
	A.append(len(_s))

print(*A)