N = int(input())
flag = False
for i in range(N):
    s = input()
    if s == "sweet" and flag:
        if i == N-1:
            print("Yes")
        else:
            print("No")
        exit()
    if s == "sweet":
        flag = True
    elif s == "salty":
        flag = False
print("Yes")