from collections import deque

N = int(input())
A = list(map(int, input().split()))

stack = deque()

for a in A:
    stack.append(a)

    while len(stack) >= 4 and stack[-1] == stack[-2] == stack[-3] == stack[-4]:
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()

print(len(stack))