N, D = map(int, input().split(" "))
S = []
for i in range(N):
	S.append(input())
	
maxhima = 0
hima = 0

for i in range(D):
	f = False

	for s in S:
		if s[i] == 'x':
			f = True
			break
	
	if f:
		maxhima = max(maxhima, hima)
		hima = 0
		continue
	hima += 1

print(max(maxhima, hima))