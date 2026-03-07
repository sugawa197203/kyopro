from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
G = defaultdict(list)
for i in range(N - 1):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

Counter = defaultdict(int)
samecount = 0
stack = [1]
watched = [False] * N
ans = [False] * N
route = []
branches = []
while stack:
    # print("===============================")
    u = stack.pop()
    route.append(u)
    if watched[u - 1]:
        continue
    watched[u - 1] = True
    
    if Counter[A[u - 1]] == 1:
        samecount += 1
    Counter[A[u - 1]] += 1
    
    # print(f"u: {u}, samecount: {samecount}, Counter: {dict(Counter)} route: {route}")

    if samecount > 0:
        ans[u - 1] = True
    neighbor = G[u]
    nowatchcount = 0
    for v in neighbor:
        if not watched[v - 1]:
            nowatchcount += 1
            stack.append(v)
    
    if nowatchcount > 1:
        branches.append((u, nowatchcount))

    # print(f"neighbor: {neighbor}, nowatchcount: {nowatchcount}, stack: {stack}, branches: {branches}")
    if nowatchcount == 0 and branches:
        backto = branches[-1][0]
        # print(f"backto: {backto}")
        while route[-1] != backto:
            w = route.pop()
            Counter[A[w - 1]] -= 1
            if Counter[A[w - 1]] == 1:
                samecount -= 1
        
        branches[-1] = (branches[-1][0], branches[-1][1] - 1)
        if branches[-1][1] == 1:
            branches.pop()
        # print(f"backto: {backto}, route: {route}, Counter: {dict(Counter)}, samecount: {samecount}")

for a in ans:
    print("Yes" if a else "No")
    
