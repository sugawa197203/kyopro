Y = int(input())

if Y % 400 == 0:
    print("366")
elif Y % 100 == 0:
    print("365")
elif Y % 4 == 0:
    print("366")
else:
    print("365")