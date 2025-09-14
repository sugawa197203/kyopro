N = int(input())
L = list(map(int, input().split()))

ok = 2

for i in range(N):
    if L[i] == 1:
        break
    ok += 1

if ok == N + 2:
    print(0)
    exit()

for i in range(N - 1, -1, -1):
    if L[i] == 1:
        break
    ok += 1

print(N - ok + 1)