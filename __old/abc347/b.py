S = input()

count = 0
d = dict()
for l in range(1, len(S)+1):
	for i in range(len(S)-l+1):
		d[S[i:i+l]] = d.get(S[i:i+l], 0) + 1

print(len(d))
