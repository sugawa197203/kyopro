N = int(input())
S = input()

ans = 0
state = 0

for s in S:
	if state == 0 and s == "#":
		state = 1
	elif state == 1 and s == ".":
		state = 2
	elif state == 2 and s == "#":
		state = 1
		ans += 1
	elif state == 0 and s == ".":
		state = 0
	elif state == 1 and s == "#":
		state = 1
	elif state == 2 and s == ".":
		state = 0

print(ans)