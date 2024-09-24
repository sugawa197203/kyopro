H, W = map(int, input().split(' '))
S = [input() for _ in range(H)]


# 0: s, 1: n, 2: u, 3: k, 4: e
snuke = "snuke"

def checksnuke(c, x, y):
    if S[x][y] == "snuke"[c]:
        return True
    return False

def get4near(x, y):
    if x == 0:
        if y == 0:
            return [(x, y + 1), (x + 1, y)]
        elif y == W - 1:
            return [(x, y - 1), (x + 1, y)]
        else:
            return [(x, y - 1), (x, y + 1), (x + 1, y)]
    elif x == H - 1:
        if y == 0:
            return [(x, y + 1), (x - 1, y)]
        elif y == W - 1:
            return [(x, y - 1), (x - 1, y)]
        else:
            return [(x, y - 1), (x, y + 1), (x - 1, y)]
    elif y == 0:
        return [(x, y + 1), (x + 1, y), (x - 1, y)]
    elif y == W - 1:
        return [(x, y - 1), (x + 1, y), (x - 1, y)]
    return [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]

def root(x, y, c):
    c = c % 5


    if x == H - 1 and y == W - 1:
        if checksnuke(c - 1, x, y):
            print('Yes')
            exit()
        else:
            print('No')
            return

    for nx, ny in get4near(x, y):
        if checksnuke(c, nx, ny):
            root(nx, ny, c + 1)

root(0, 0, 1)
print('No')

