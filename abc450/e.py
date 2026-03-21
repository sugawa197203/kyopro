from collections import defaultdict
from bisect import bisect_left, bisect_right

X = input()
Y = input()
Q = int(input())

fibo = [0] * 88
fibo[0] = 1
fibo[1] = 1
for i in range(2, 88):
    fibo[i] = fibo[i-1] + fibo[i-2]

fiboaccum = [(0, 1)]
for i in range(1, 88):
    fiboaccum.append((i, fiboaccum[-1][1] + fibo[i]))

Xcounts = [0] * 88
Ycounts = [0] * 88
Xcounts[0] = 1
Ycounts[1] = 1

for i in range(2, 88):
    Xcounts[i] = Xcounts[i-1] + Xcounts[i-2]
    Ycounts[i] = Ycounts[i-1] + Ycounts[i-2]

Xcountsaccum = [0] * 88
Ycountsaccum = [0] * 88
Xcountsaccum[0] = Xcounts[0]
Ycountsaccum[0] = Ycounts[0]
for i in range(1, 88):
    Xcountsaccum[i] = Xcountsaccum[i-1] + Xcounts[i]
    Ycountsaccum[i] = Ycountsaccum[i-1] + Ycounts[i]

Xalphabets = defaultdict(int)
Yalphabets = defaultdict(int)
for i in range(len(X)):
    Xalphabets[X[i]] += 1
for i in range(len(Y)):
    Yalphabets[Y[i]] += 1

Xalphabetsaccum = {c: [0] * 88 for c in Xalphabets}
Yalphabetsaccum = {c: [0] * 88 for c in Yalphabets}
Xalphabetsaccum[X[0]][0] = 1

for c in Xalphabets:
    Xalphabetsaccum[c][0] = Xalphabets[c] * Xcounts[0]
    for i in range(1, 88):
        Xalphabetsaccum[c][i] = Xalphabetsaccum[c][i-1] + Xalphabets[c] * Xcounts[i]
for c in Yalphabets:
    Yalphabetsaccum[c][0] = Yalphabets[c] * Ycounts[0]
    for i in range(1, 88):
        Yalphabetsaccum[c][i] = Yalphabetsaccum[c][i-1] + Yalphabets[c] * Ycounts[i]

print(Xcounts)
print(Ycounts)

print(fibo, len(str(fibo[-1])))
print(fiboaccum, len(str(fiboaccum[-1][1])))

for _ in range(Q):
    L, R, C = input().split()
    L, R = int(L) - 1, int(R) - 1
    ans = 0

    
    left = bisect_right(fiboaccum, L, key=lambda x: x[1])
    right = bisect_left(fiboaccum, R, key=lambda x: x[1])
    print(left, right)
    print(Xcountsaccum[left], Xcountsaccum[right], Ycountsaccum[left], Ycountsaccum[right])
    ans += Xalphabets[C] * (Xcountsaccum[right] - Xcountsaccum[left])
    ans += Yalphabets[C] * (Ycountsaccum[right] - Ycountsaccum[left])




# A000045 = lambda n: (1<<((n+1)*(n+1)))//((4<<(2*n))-(2<<n)-1)&((2<<n)-1)

# print(A000045(84), len(str(A000045(84))))
[(0, 1), (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13), (7, 21), (8, 34), (9, 55), (10, 89), (11, 144), (12, 233), (13, 377), (14, 610), (15, 987), (16, 1597), (17, 2584), (18, 4181), (19, 6765), (20, 10946), (21, 17711), (22, 28657), (23, 46368), (24, 75025), (25, 121393), (26, 196418), (27, 317811), (28, 514229), (29, 832040), (30, 1346269), (31, 2178309), (32, 3524578), (33, 5702887), (34, 9227465), (35, 14930352), (36, 24157817), (37, 39088169), (38, 63245986), (39, 102334155), (40, 165580141), (41, 267914296), (42, 433494437), (43, 701408733), (44, 1134903170), (45, 1836311903), (46, 2971215073), (47, 4807526976), (48, 7778742049), (49, 12586269025), (50, 20365011074), (51, 32951280099), (52, 53316291173), (53, 86267571272), (54, 139583862445), (55, 225851433717), (56, 365435296162), (57, 591286729879), (58, 956722026041), (59, 1548008755920), (60, 2504730781961), (61, 4052739537881), (62, 6557470319842), (63, 10610209857723), (64, 17167680177565), (65, 27777890035288), (66, 44945570212853), (67, 72723460248141), (68, 117669030460994), (69, 190392490709135), (70, 308061521170129), (71, 498454011879264), (72, 806515533049393), (73, 1304969544928657), (74, 2111485077978050), (75, 3416454622906707), (76, 5527939700884757), (77, 8944394323791464), (78, 14472334024676221), (79, 23416728348467685), (80, 37889062373143906), (81, 61305790721611591), (82, 99194853094755497), (83, 160500643816367088), (84, 259695496911122585), (85, 420196140727489673), (86, 679891637638612258), (87, 1100087778366101931)]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            