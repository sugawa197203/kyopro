import numpy as np
N = int(input())

ans = np.ones((1, 1), dtype=int)

def stamp(a:np.ndarray, b:np.ndarray, i:int, j:int):
    for x in range(b.shape[0]):
        for y in range(b.shape[1]):
            a[i + x][j + y] = b[x][y]
    
    print(a.shape)
    print(a)
    print(b.shape)
    print(b)

for i in range(N):
    _ans = ans.copy()
    ans = np.zeros((3**i, 3**i), dtype=int)
    print("------------")
    print(ans)
    print(_ans)
    print("------------")
    for j in range(i+1):
        for k in range(i+1):
            print("----")
            print(i, j, k)
            print(ans)
            print(_ans)
            print("----")
            stamp(ans, _ans, j * 3, k * 3)
            

print("\n".join("".join(("#" if r == 1 else ".") for r in row) for row in ans))
