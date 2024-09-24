N, M = map(int, input().split())
house = [0] * N
for _ in range(M):
    a, b = input().split()
    a = int(a) - 1
    if b == "M":
        if house[a] == 0:
            print("Yes")
            house[a] = 1
            continue
    print("No")
    