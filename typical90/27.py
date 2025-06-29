N = int(input())
S = set()
for i in range(N):
    s = input()
    if s not in S:
        S.add(s)
        print(i+1)
