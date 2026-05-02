X = int(input())

saikoro = [1, 2, 3, 4, 5, 6]

arieru = set()

for i in saikoro:
    for j in saikoro:
        for k in saikoro:
            arieru.add(i + j + k)

if X in arieru:
    print("Yes")
else:
    print("No")
