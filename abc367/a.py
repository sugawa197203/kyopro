A, B, C = map(int, input().split())

if B < C:
    if B < A < C:
        print("No")
    else:
        print("Yes")
else:
    C += 24
    A += 24
    if B < A < C:
        print("No")
    else:
        print("Yes")