N = int(input())
A = list(input().split())
intA = [int(a) for a in A]
lenA = [len(a) for a in A]

s = 0
# keta = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(N)]
keta = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for lena in lenA[1:]:
	keta[lena] += 1

for i, a in enumerate(A[:-1]):
	if i != 0:
		keta[len(a)] -= 1
	for j, _keta in enumerate(keta[1:]):
		s += intA[i] * (10**(j+1) * _keta)
		#print(intA[i], (10**(j+1) , _keta), intA[i] * (10**(j+1) * _keta))

for i, a in enumerate(A[1:]):
	s += (i + 1) * int(a)

print(s % 998244353)

