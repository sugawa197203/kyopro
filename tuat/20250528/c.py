N, K = map(int, input().split())
A = list(map(int, input().split()))

pos = 1
f = [-1] * (N + 1)
f[pos] = 0
cnt = 0
length = 0
offset = 0
while True:
    cnt += 1
    pos = A[pos - 1]
    if f[pos] >= 0:
        length = cnt - f[pos]
        offset = f[pos]
        break
    f[pos] = cnt

if offset + length >= K:
    pos = 1
    for i in range(K):
        pos = A[pos - 1]

    print(pos)
    exit()

K -= offset
K %= length
for i in range(K):
    pos = A[pos - 1]
print(pos)
