N = int(input())
p = list(map(int, input().split()))

distances = [0] * N
rotate1 = {}
rotate2 = {}
rotate3 = {}

for i, _p in enumerate(p):
    a = i-_p
    if a < 0:
        a = -a
    
    if a in rotate1:
        rotate1[a] += 1
    else:
        rotate1[a] = 1
    
    a = i-_p+1
    if a < 0:
        a = -a
    if a in rotate2:
        rotate2[a] += 1
    else:
        rotate2[a] = 1
    
    a = i-_p-1
    if a < 0:
        a = -a
    if a in rotate3:
        rotate3[a] += 1
    else:
        rotate3[a] = 1

print(rotate1)
print(rotate2)
print(rotate3)
