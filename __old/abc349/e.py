import itertools
A:list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0]
PATTERN:list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8]
for i in range(3):
	a = list(map(int, input().split()))
	for j in range(3):
		A[3 * i + j] += a[j]

WHITE = 0
RED = 1
BLUE = 2
START_COLOR:list[int] = [WHITE] * 9

def check(color:list[int]) -> int:
	for i in range(3):
		if color[3 * i] == color[3 * i + 1] == color[3 * i + 2]:
			return color[3 * i]
		if color[i] == color[i + 3] == color[i + 6]:
			return color[i]
	if color[0] == color[4] == color[8]:
		return color[0]
	if color[2] == color[4] == color[6]:
		return color[2]
	return -1

r = 0
b = 0
d = 0

stack = []

stack.append(([1, 0, 0, 0, 0, 0, 0, 0, 0], RED))
stack.append(([0, 1, 0, 0, 0, 0, 0, 0, 0], RED))
stack.append(([0, 0, 1, 0, 0, 0, 0, 0, 0], RED))
stack.append(([0, 0, 0, 1, 0, 0, 0, 0, 0], RED))
stack.append(([0, 0, 0, 0, 1, 0, 0, 0, 0], RED))
stack.append(([0, 0, 0, 0, 0, 1, 0, 0, 0], RED))
stack.append(([0, 0, 0, 0, 0, 0, 1, 0, 0], RED))
stack.append(([0, 0, 0, 0, 0, 0, 0, 1, 0], RED))
stack.append(([0, 0, 0, 0, 0, 0, 0, 0, 1], RED))

while len(stack) > 0:
	color, turn = stack.pop()
	result = check(color)
	if result == RED:
		r += 1
	elif result == BLUE:
		b += 1
	elif turn == 9:
		redScore = sum([A[i] for i in range(9) if color[i] == RED])
		blueScore = sum([A[i] for i in range(9) if color[i] == BLUE])
		if redScore >= blueScore:
			r += 1
		else:
			b += 1
	else:
		for i in range(9):
			if color[i] == WHITE:
				new_color = color.copy()
				new_color[i] = turn % 2 + 1
				stack.append((new_color, turn + 1))

print("Takahashi" if r >= b else "Aoki")