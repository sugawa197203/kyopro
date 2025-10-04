N, Q = map(int, input().split())

minimum = 1

V = list(range(1, N + 1))
C = [1] * N

for _ in range(Q):
    x, y = map(int, input().split())

    if x < minimum:
        print(0)
        continue
    sum = 0
    for i in range(minimum - 1, x):
        sum += C[i]
        C[i] = 0
    
    C[y - 1] += sum

    if minimum <= x:
        minimum = x + 1
    
    print(sum)
    

