from collections import defaultdict

N = int(input())

A = [list(map(int, input().split())) for _ in range(N-1)]

AA = []
print("\n".join(" ".join(map(str, a)) for a in A))
for i in range(N-1):
    for j in range(N-i-1):
        AA.append((A[i][j], i, j+i+1))

AA.sort(key=lambda x: x[0])
print(AA)

Tree = defaultdict(list)

minimum = AA[0]

for u in range(N-1):

    _A = [(w, u) for u, w in zip(A[u], range(u+1, N))]
    print("_A:", _A)

    minu = min(_A, key=lambda x: x[1])
    for v, w in _A:
        if w == minu[1]:
            Tree[u].append((v, w))
            Tree[v].append((u, w))



    print(Tree)


# queue = deque([0])
# visited = {0}
# while queue:
#     u = queue.popleft()
    
#     for v, w in Tree[u]:
#         if v in visited:
#             continue

#         visited.add(v)
#         queue.append(v)

        
