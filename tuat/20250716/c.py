N = int(input())

left, right = [], []
for _ in range(N):
	l, r = map(int, input().split())
	left.append(l)
	right.append(r)

left.sort()
right.sort()
leftidx = 0
rightidx = 0
count = 0
val = 0

for i in range(1, 2 * (2 * 10**5) + 1):
	while leftidx < N and left[leftidx] == i:
		if count == 0:
			print(left[leftidx], end=' ')
		count += 1
		leftidx += 1
	
	while rightidx < N and right[rightidx] == i:
		count -= 1
		if count == 0:
			print(right[rightidx])
		rightidx += 1
		

