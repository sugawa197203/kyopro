N, c1, c2 = input().split()
N = int(N)
S = input()

ans = []

for s in S:
	if s == c1:
		ans.append(c1)
	else:
		ans.append(c2)

print(''.join(ans))
