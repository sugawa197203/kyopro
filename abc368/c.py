N = int(input())
H = list(map(int, input().split()))

t = 0

for h in H:
    shou, amari = divmod(h, 5)
    t += shou * 3
    
    while amari > 0:
        t += 1
        if t % 3 == 0:
            amari -= 3
        else:
            amari -= 1

print(t)
