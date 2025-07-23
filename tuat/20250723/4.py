N, Q = map(int, input().split())

trains = [[-1, -1] for _ in range(N)]

for _ in range(Q):
    q, *xy = map(int, input().split())
    if q == 1:
        x, y = xy
        trains[x - 1][1] = y
        trains[y - 1][0] = x
    elif q == 2:
        x, y = xy
        trains[x - 1][1] = -1
        trains[y - 1][0] = -1
    elif q == 3:
        x = xy[0]
        while True:
            if trains[x - 1][0] == -1:
                break
            x = trains[x - 1][0]
        ans = [x]
        while trains[x - 1][1] != -1:
            x = trains[x - 1][1]
            ans.append(x)

        print(len(ans), *ans)
