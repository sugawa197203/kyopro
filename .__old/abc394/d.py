S = input()

stack = []

for c in S:
	if c in ["(", "[", "<"]:
		stack.append(c)
	else:
		if len(stack) == 0:
			print("No")
			exit()
		if c == ")" and stack[-1] == "(":
			stack.pop()
		elif c == "]" and stack[-1] == "[":
			stack.pop()
		elif c == ">" and stack[-1] == "<":
			stack.pop()
		else:
			print("No")
			exit()

if len(stack) == 0:
	print("Yes")
else:
	print("No")
