Q = int(input())
stack = [0] * 100
for _ in range(Q):
	q = list(map(int, input().split()))
	if len(q) == 2:
		stack.append(q[1])
	else:
		print(stack.pop())