

def main():
    N, H = map(int, input().split())
    tlu = [tuple(map(int, input().split())) for _ in range(N)]
    tlu.sort(key=lambda x: x[0])

    ll, uu = H, H
    tt = 0
    for t, l, u in tlu:
        ll = max(0, ll - (t - tt))
        uu = uu + (t - tt)
        if u < ll or uu < l:
            print("No")
            return
        ll = max(ll, l)
        uu = min(uu, u)
        tt = t
    
    print("Yes")


T = int(input())
for _ in range(T):
    main()
