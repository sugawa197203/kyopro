N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

pos = 0

pueue = [0]
ignore = {0}
dX = set(B)
while pueue:
    pos = pueue.pop(0)
    if pos == X:
        print("Yes")
        exit()

    for a in A:
        if ((pos + a) not in ignore) and ((pos + a) not in dX) and ((pos + a <= X)):
            pueue.append(pos + a)
            ignore.add(pos + a)

print("No")
