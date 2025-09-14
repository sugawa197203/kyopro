N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = dict()

ruisekihash = []
h = 0
for i in range(N):
    h ^= A[i]
    ruisekihash.append(h)

def caloc(l, r):
    

for q in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    l = ruisekihash[L]
    r = ruisekihash[R] ^ A[R]

