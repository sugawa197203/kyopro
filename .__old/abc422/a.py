S = input().split("-")

a, b = map(int, S)

if b == 8:
    print(f"{a+1}-1")
else:
    print(f"{a}-{b+1}")

