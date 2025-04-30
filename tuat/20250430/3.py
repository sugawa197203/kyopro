x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

manhattan = abs(x1 - x2) + abs(y1 - y2)

if manhattan <= 3 or (x1 + x2 == y1 + y2):
    print("1")
    exit()

if manhattan % 2 == 0:
    print("2")
    exit()

x3, y3 = abs(x1 - x2), abs(y1 - y2)


