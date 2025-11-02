from sortedcontainers import SortedList
N = int(input())
X = list(map(int, input().split()))

pos = SortedList()
pos.add((0, 10**9+1))
ans = 10**9+1
buf = []

for x in X:
    pos.add((x, 0))
    idx = pos.index((x, 0))
    left = pos[idx - 1]
    leftdist = abs(x - left[0])
    if leftdist < left[1]:
        ans += leftdist - left[1]
        pos.discard(left)
        pos.add((left[0], leftdist))

    rightdist = float('inf')
    if idx + 1 < len(pos):
        right = pos[idx + 1]
        rightdist = abs(x - right[0])
        if rightdist < right[1]:
            ans += rightdist - right[1]
            pos.discard(right)
            pos.add((right[0], rightdist))
    
    dist = min(leftdist, rightdist)
    pos.discard((x, 0))
    pos.add((x, dist))
    ans += dist
    buf.append(ans)

print('\n'.join(map(str, buf)))

