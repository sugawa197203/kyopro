from bisect import bisect_left, bisect_right
from collections import deque

N, M = map(int, input().split())
S = input()
T = input()

L = [0] * M
R = [0] * M

for i in range(M):
    L[i], R[i] = map(int, input().split())
    L[i] -= 1
    

L.sort()
R.sort()
L = deque(L)
R = deque(R)

isS = True
i = 0

ans = []
while i < N:
    while L and L[0] == i:
        L.popleft()
        isS = not isS

    while R and R[0] == i:
        R.popleft()
        isS = not isS
        
    if isS:
        ans.append(S[i])
    else:
        ans.append(T[i])
    i += 1
print(''.join(ans))
