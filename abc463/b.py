N, X = input().split()
N = int(N)
S = [input() for _ in range(N)]

x = ["A", "B", "C", "D", "E"]

for s in S:
    for _x, c in zip(x, s):
        if c == "o" and _x == X:
            print("Yes")
            exit()

print("No")
