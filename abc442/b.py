Q = int(input())

v = 0
p = False

for _ in range(Q):
    a = int(input())
    if a == 1:
        v += 1
    elif a == 2:
        v = max(0, v - 1)
    else:
        p = not p
    
    print("Yes" if (v > 2 and p) else "No")
