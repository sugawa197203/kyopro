from collections import deque

N = int(input())
A = list(map(int, input().split()))


inverse = False

ans = deque()

for a in A:
    if inverse:
        ans.append(a)
    else:
        ans.appendleft(a)
    inverse = not inverse

if not inverse:
    ans.reverse()

print(*ans)
