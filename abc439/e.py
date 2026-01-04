from networkx import DiGraph
from sortedcontainers import SortedDict

N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

G = DiGraph()

for i in range(N):
    G.add_edge("S", i, capacity=1)

rightAacc = SortedDict()
rightAacc[0] = 0
rightbefor = 0
leftAacc = SortedDict()
leftAacc[0] = 0
leftbefor = 0
for a, b in sorted(AB, key=lambda x: x[0]):
    if a <= b:
        rightAacc[a] = rightAacc[rightbefor] + 1
        rightbefor = a
    else:
        leftAacc[a] = leftAacc[leftbefor] + 1
        leftbefor = a


rightBacc = SortedDict()
rightBacc[0] = 0
rightbefor = 0
leftBacc = SortedDict()
leftBacc[0] = 0
leftbefor = 0
for a, b in sorted(AB, key=lambda x: x[1]):
    if a <= b:
        rightBacc[b] = rightBacc[rightbefor] + 1
        rightbefor = b
    else:
        leftBacc[b] = leftBacc[leftbefor] + 1
        leftbefor = b

print(f"rightAacc: {rightAacc}")
print(f"leftAacc: {leftAacc}")
print(f"rightBacc: {rightBacc}")
print(f"leftBacc: {leftBacc}")

for i, (a, b) in enumerate(AB):
    print("----")
    print(a, b)
    if a <= b:
        _a = rightAacc.peekitem(rightAacc.bisect_right(a) - 1)[1]
        _b = rightBacc.peekitem(rightBacc.bisect_right(b) - 1)[1]
        print(f"_a: {_a}, _b: {_b}")
        print(f"diff {_a - _b}")
    else:
        _a = leftAacc.peekitem(leftAacc.bisect_right(a) - 1)[1]
        _b = leftBacc.peekitem(leftBacc.bisect_right(b) - 1)[1]
        print(f"_a: {_a}, _b: {_b}")
        print(f"diff {_a - _b}")

