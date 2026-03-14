N, M = map(int, input().split())
A = list(map(int, input().split()))
Q = int(input())

count = [(0, i) for i in range(M)]

for a in A:
    count[a - 1] = (count[a - 1][0] + 1, a - 1)

sortedcount = sorted(count)
print(sortedcount)

appends = []
i = 0
beforecount = sortedcount[0][0]
while len(appends) < M:
    print(f'i={i}, sortedcount={sortedcount}, beforecount={beforecount}')
    if sortedcount[i][0] == beforecount:
        appends.append(sortedcount[i][1])
        sortedcount[i] = (sortedcount[i][0] + 1, sortedcount[i][1])
        i += 1
    else:
        beforecount = sortedcount[i][0]
        appends.append(sortedcount[i][1])
        sortedcount[i] = (sortedcount[i][0] + 1, sortedcount[i][1])
        i = 0

print(appends)
print(sortedcount)

K = len(appends)

for _ in range(Q):
    X = int(input())
    if X <= N:
        print(A[X - 1])
    elif X <= N + K:
        print(appends[X - N - 1])
    else:
        print((X - N - K - 1) % M + 1)
