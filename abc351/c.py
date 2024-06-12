N = int(input())
A = list(map(int, input().split()))

length = -1
l = [0] * N

for i, a in enumerate(A):
	length += 1
	l[length] = a
	while True:
		if length <= 0:
			break
		if l[length] != l[length-1]:
			break
		l[length-1] += 1
		length -= 1

print(length+1)