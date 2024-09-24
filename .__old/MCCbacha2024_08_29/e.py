N, M = map(int, input().split())
A, B = [], []
for i in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

table = dict()

for a, b in zip(A, B):
    l = table.get(a, [])
    if len(l) == 2:
        print('No')
        exit()
    if b not in l:
        l.append(b)
    table[a] = l
    
    l = table.get(b, [])
    
    if len(l) == 2:
        print('No')
        exit()
    if a not in l:
        l.append(a)
    table[b] = l

wathced = set()

for k, v in table:
    if k in wathced:
        continue
    wathced.add(k)
    stack = [k]
    while stack:
        n = stack.pop()
        for i in table[n]:
            if i in wathced:
                continue
            wathced.add(i)
            stack.append(i)
    

print('Yes')