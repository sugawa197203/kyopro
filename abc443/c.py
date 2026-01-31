N, T = map(int, input().split())
A = list(map(int, input().split()))

t = 0
openat = 0

if N == 0:
    print(T)
    exit()

for a in A:
    if a < openat:
        continue
    t += a - openat
    openat = a + 100

if openat < T:
    t += T - openat

print(t)
