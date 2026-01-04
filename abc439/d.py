from sortedcontainers import SortedDict

N = int(input())
A = list(map(int, input().split()))

rightcount = SortedDict()
leftcount = SortedDict()
for a in A:
    if a in rightcount:
        rightcount[a] += 1
    else:
        rightcount[a] = 1

ans = 0
for i, a in enumerate(A):
    rightcount[a] -= 1
    if rightcount[a] == 0:
        del rightcount[a]

    if a % 5 == 0:
        seven = a // 5 * 7
        three = a // 5 * 3
        if seven in leftcount and three in leftcount:
            ans += leftcount[seven] * leftcount[three]
        if seven in rightcount and three in rightcount:
            ans += rightcount[seven] * rightcount[three]
    
    if a in leftcount:
        leftcount[a] += 1
    else:
        leftcount[a] = 1

print(ans)
