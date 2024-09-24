

N = int(input())
MG = int(input())
G = dict()
for i in range(MG):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    l = G.get(v1, [])
    l.append(v2)
    G[v1] = l
    l = G.get(v2, [])
    l.append(v1)
    G[v2] = l

MH = int(input())
H = dict()
for i in range(MH):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    l = H.get(v1, [])
    l.append(v2)
    H[v1] = l
    l = H.get(v2, [])
    l.append(v1)
    H[v2] = l

A = []
for i in range(N - 1):
    A.append(list(map(int, input().split())))

def graphDoukei(graphA: dict, graphB: dict, start: int):
    visited = set()
    stackA = [0]
    stackB = [start]
    while stackA:
        nodeA = stackA.pop()
        nodeB = stackB.pop()
        if nodeA in visited:
            continue
        visited.add(nodeA)
        nextnodeA = graphA.get(nodeA, [])
        nextnodeA.sort()
        nextnodeB = graphB.get(nodeB, [])
        nextnodeB.sort()
        print(nodeA, nextnodeA, nextnodeB)
        if len(nextnodeA) != len(nextnodeB):
            return False
        stackA.extend(nextnodeA)
        stackB.extend(nextnodeB)
    return True

def isdoukei(graphA: dict, graphB: dict):
    for i in range(N):
        r = graphDoukei(graphA, graphB, i)
        print(i, r)
        if graphDoukei(graphA, graphB, i):
            return True
    return False

print(G, H)
print(isdoukei(G, H))
