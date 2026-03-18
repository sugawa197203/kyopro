N = int(input())
S = input()
T = []
i = 0

while i < N - 2:
    if S[i:i + 3] == "TAT":
        T += ["TUA"]
        i += 2
    else:
        T += [S[i]]
        i += 1

T += [S[i:]]
# print(T)
T = "".join(T)
print(T)
