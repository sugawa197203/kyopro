from collections import Counter
from math import ceil

def solve(S: str):
    N = len(S)
    C = sorted(Counter(S).items(), key=lambda x: x[1], reverse=True)
    topcount = C[0][1]
    othercount = sum([x[1] for x in C[1:]])
    if topcount <= othercount + 1:
        print("Yes")
    else:
        print("No")
        return
    left = []
    leftsum = 0
    right = []
    rightsum = 0
    half = int(ceil(N / 2))
    isLeft = True

    if half == 0:
        print(S)
        return

    for c, count in C:
        if isLeft:
            appendable = min(count, half - leftsum)
            left.append((c, appendable))
            leftsum += appendable
            if leftsum == half:
                isLeft = False
                if count - appendable > 0:
                    right.append((c, count - appendable))
                    rightsum += count - appendable
        else:
            appendable = min(count, N - half - rightsum)
            right.append((c, appendable))
            rightsum += appendable
    
        # print(left, right, half, leftsum, rightsum)

    ans = ""
    while left or right:
        if left:
            c, count = left[-1]
            ans += c
            if count == 1:
                left.pop()
            else:
                left[-1] = (c, count - 1)
        if right:
            c, count = right[-1]
            ans += c
            if count == 1:
                right.pop()
            else:
                right[-1] = (c, count - 1)
    
    print(ans)

T = int(input())
for _ in range(T):
    solve(input())