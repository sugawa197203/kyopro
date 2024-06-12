N, K = map(int, input().split())
A = list(map(int, input().split()))

car = 0
count = 0

while len(A) > 0:
	a = A.pop(0)
	car += a
	if car > K:
		car = 0
		count += 1
		A.insert(0, a)

print(count+1)
