S = list(map(int, input().split(' ')))

if not (S[0] <= S[1] <= S[2] <= S[3] <= S[4] <= S[5] <= S[6] <= S[7]):
	print('No')
	exit()

for s in S:
		if not (100 <= s <= 675 and s % 25 == 0):
			print('No')
			exit()

print('Yes')
			