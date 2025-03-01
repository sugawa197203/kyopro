N, Q = map(int, input().split())

hato = list(range(N))
su = list(range(N))
suind = list(range(N))

for _ in range(Q):
    q, *ab = list(map(int, input().split()))
    # print("========================")
    # print("q, ab:", q, ab)
    # print("hato:", hato)
    # print("su:", su)
    
    if q == 1:
        a, b = ab
        a, b = a - 1, b - 1
        hato[a] = su[b]

    elif q == 2:
        a, b = ab
        a, b = a - 1, b - 1
        su[a], su[b] = su[b], su[a]
        suind[su[a]], suind[su[b]] = suind[su[b]], suind[su[a]]

    else:
        a = ab[0]
        a = a - 1
        print(suind[hato[a]] + 1)
