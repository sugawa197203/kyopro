N = int(input())

d = dict()

for i in range(N):
	S = input()
	d[len(S)] = S

cat = ""
for k in sorted(d.keys()):
	cat += d[k]

print(cat)
