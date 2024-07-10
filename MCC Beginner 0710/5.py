N = int(input())
A = list(map(int, input().split()))

A.sort()
ruisekiwa = [0] * N
ruisekiwa[0] = A[0]
for i in range(1, N):
	ruisekiwa[i] = ruisekiwa[i - 1] + A[i]
sum = 0

for i in range(N - 1):
	sum += ruisekiwa[-1] - ruisekiwa[i] - A[i] * (N - i - 1)
	
print(sum)