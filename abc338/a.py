S = input()

if not (ord('A') <= ord(S[0]) <= ord('Z')):
	print("No")
	exit()

for s in S[1:]:
	if not (ord('a') <= ord(s) <= ord('z')):
		print("No")
		exit()

print("Yes")