import bisect

H, W, Q = map(int, input().split())
R, C = [0] * Q, [0] * Q
for i in range(Q):
    R[i], C[i] = map(int, input().split())

wall = [[True] * W for _ in range(H)]
row_walls = {i: list(range(1, W+1)) for i in range(1, H+1)}
col_walls = {i: list(range(1, H+1)) for i in range(1, W+1)}

def iswall(r, c):
    return wall[r-1][c-1]

for r, c in zip(R, C):
    print("-----")
    print(wall)
    print(r, c)
    print(row_walls)
    print(col_walls)
    if iswall(r, c):
        wall[r-1][c-1] = False
        row_walls[r].remove(c)
        col_walls[c].remove(r)
        continue

    up = bisect.bisect_left(col_walls[c], r)
    down = bisect.bisect_right(col_walls[c], r)
    left = bisect.bisect_left(row_walls[r], c)
    right = bisect.bisect_right(row_walls[r], c)

    print(up, down, left, right)

    f = True
    print(wall)
    if up != 0:
        wall[r-1][col_walls[c].pop(up)-1] = False
        
        f = False
    print(wall, len(col_walls[c]))
    if down <= len(col_walls[c]):
        wall[col_walls[c].pop(down if f else down-1)-1][c-1] = False
        
    f = True
    print(wall)
    if left != 0:
        a = row_walls[r].pop(left-1)-1
        print
        wall[c-1][a] = False
        
        f = False
    print(wall, len(row_walls[r]))
    if right <= len(row_walls[r]):
        wall[row_walls[r].pop(right if f else right-1)-1][c] = False
        
    print(wall)
    

print(row_walls)
print(col_walls)
remaining_walls = sum(len(walls) for walls in row_walls.values())
print(remaining_walls)