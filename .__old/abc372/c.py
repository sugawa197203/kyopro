N, Q = map(int, input().split())
S = list(input())

ABCcount = 0

for i in range(N-2):
    if S[i:i+3] == ["A","B","C"]:
        ABCcount += 1    

for _ in range(Q):
    x, c = input().split()
    x = int(x) - 1
    if S[x] == c:
        print(ABCcount)
        continue

    if S[x:x+3] == ["A","B","C"]:
        ABCcount -= 1
    elif S[x-1:x+2] == ["A","B","C"]:
        ABCcount -= 1
    elif S[x-2:x+1] == ["A","B","C"]:
        ABCcount -= 1

    S[x] = c
    
    if S[x:x+3] == ["A","B","C"]:
        ABCcount += 1
    elif S[x-1:x+2] == ["A","B","C"]:
        ABCcount += 1
    elif S[x-2:x+1] == ["A","B","C"]:
        ABCcount += 1
    print(ABCcount)
