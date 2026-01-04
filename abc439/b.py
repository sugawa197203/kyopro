N = input()

length = len(N)

while length > 1:
    N = str(sum(int(digit)**2 for digit in N))
    length = len(N)

if N == "1":
    print("Yes")
else:
    print("No")
