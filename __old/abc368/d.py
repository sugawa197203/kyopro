N, K = map(int, input().split())
A, B = [0]*N, [0]*N
for i in range(N-1):
    A[i], B[i] = map(int, input().split())
V = list(map(int, input().split()))

edge:dict[int, list] = dict()
for n in range(N):
    edge[n] = []

for n in range(N-1):
    edge[A[n]-1].append(B[n])
    edge[B[n]-1].append(A[n])

memo = [False]*N
memo[V[0]-1] = True

for v in V[1:]:

    stack = edge[v - 1]
    root = [v]
    watched = set()
    watched.add(v)
    while stack:
        node = stack.pop()

            
        if memo[node-1]:
            break
        for r in root[::-1]:
            nextnode = [n for n in edge[node-1] if n not in watched]
            if len(nextnode) == 0 and r != v:
                root.pop()
        if node in watched:
            continue
        watched.add(node)
        nextnode = [n for n in edge[node-1] if n not in watched]
        if len(nextnode) == 0:
            continue
        root.append(node)
        stack += nextnode
        
    print(root)
    for r in root:
        memo[r-1] = True

print(sum(memo))
    