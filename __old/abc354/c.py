import bisect
N = int(input())
A, C = [0] * N, [0] * N
for i in range(N):
	A[i], C[i] = map(int, input().split())

enables = [True] * N
Akey = list(range(N))
Ckey = list(range(N))
Akey.sort(key=lambda x: A[x])
Ckey.sort(key=lambda x: C[x], reverse=True)

for i in range(N):
	if enables[i]:
		ai = A[i]
		ci = C[i]
		Aleft = bisect.bisect_right(Akey, ai, key=lambda x: A[x])
		Cleft = bisect.bisect_left(Ckey, ci, key=lambda x: C[x])
		print(Aleft, Cleft)

print(sum(filter(lambda x: x, enables)))
print(" ".join(map(str, [i+1 for i in range(N) if enables[i]])))
