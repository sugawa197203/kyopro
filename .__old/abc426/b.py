S = input()

ss = list(set(S))

s0 = ss[0]
s1 = ss[1]

if S.count(s0) == 1:
    print(s0)
else:
    print(s1)