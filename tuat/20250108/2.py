S = input()

ans = 0

if len(S) == 1:
    print(0)
    exit()

if len(S) == 2:
    if S[0] != S[1]:
        print(0)
    else:
        print(2)
    exit()

if len(S) == 3:
    if S[0] == S[1] or S[1] == S[2]:
        print(2)
    else:
        print(0)
    exit()

stack = []
stack.append(S[0])

for s in S[1:]:
    if not stack:
        stack += s
        continue
    if stack[-1] == s:
        stack += s
    else:
        ans += 2
        stack.pop()

print(ans)
