S = input()

alphabetCount = dict()

for _s in "abcdefghijklmnopqrstuvwxyz":
	alphabetCount[_s] = 0

for s in S:
	alphabetCount[s] += 1

alphabetCount = sorted(alphabetCount.items(), key=lambda x:x[1], reverse=True)

m = alphabetCount[0][1]

t = []

for a in alphabetCount:
	if a[1] == m:
		t.append(a[0])

t = sorted(t)
print(t[0])
