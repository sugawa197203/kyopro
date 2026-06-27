H, W, Q = map(int, input().split())
RCX = []
for _ in range(Q):
    r, c, x = input().split()
    RCX.append((int(r) - 1, int(c) - 1, x))

ans = [['A' for _ in range(W)] for _ in range(H)]

lock = [[False for _ in range(W)] for _ in range(H)]

RCX = reversed(RCX)
for r, c, x in RCX:
    if lock[r][c]:
        continue
    for _h in range(r, -1, -1):
        if lock[_h][c]:
            break
        for _w in range(c, -1, -1):
            if lock[_h][_w]:
                break
            ans[_h][_w] = x
            lock[_h][_w] = True

print('\n'.join(''.join(row) for row in ans))
