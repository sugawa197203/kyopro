S = input()
if S[0] != '<':
	print('No')
	exit()

if S[-1] != '>':
	print('No')
	exit()

S = S[1:-1]

for i in range(len(S)):
	if S[i] != '=':
		print('No')
		exit()

print('Yes')