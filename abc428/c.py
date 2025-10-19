from collections import deque

Q = int(input())

stack = deque()
S = deque()
PUSH = 1
POP = 2
for _ in range(Q):
    q = input().split()
        
    if q[0] == "1":
        q = q[1]
        if not stack:
            stack.append(q)
            S.append((PUSH, q))
        elif q == ")" and stack[-1] == "(":
            stack.pop()
            S.append((POP, "("))
        else:
            stack.append(q)
            S.append((PUSH, q))
    elif q[0] == "2":
        if S[-1][0] == PUSH:
            S.pop()
            if stack:
                stack.pop()
        else:
            S.pop()
            stack.append("(")

    # print(f"stack: {stack}, S: {S}")
    if not stack:
        print("Yes")
    else:
        print("No")
            
