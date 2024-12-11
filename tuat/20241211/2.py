N = int(input())
H = list(map(int, input().split()))

higth = H[0]
for h in H[1:]:
    if h <= higth:
        print(higth)
        break
    higth = h
else:
    print(higth)