a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

if b - a <= k and c - a <= k and d - a <= k and e - a <= k and c - b <= k and d - b <= k and e - b <= k and d - c <= k and e - c <= k and e - d <= k:
    print('Yay!')
else:
    print(':(')