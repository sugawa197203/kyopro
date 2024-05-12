N = int(input())
sA = input().split()
keta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
A = [int(a) for a in sA]
for sa in sA:
	keta[len(sa)] += 1
s = 0
for a in A:
	s += a * (N - 1)
sub = 0
for i in range(10):
	for j in range(i + 1, 10):
		if i + j >= 8 and keta[i] > 0 and keta[j] > 0:
			sub += 1
			print(i, j, keta[i], keta[j])

print(s - sub * 10 ** 8)

print(sub)
print(keta)