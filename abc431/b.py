X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
have = set()
for _ in range(Q):
    p = int(input())
    if p in have:
        X -= W[p - 1]
        print(X)
        have.remove(p)
    else:
        X += W[p - 1]
        print(X)
        have.add(p)

