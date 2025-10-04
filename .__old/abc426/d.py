

def solve(N:int, S:list[int]):
    
    onecount = S.count(1)
    zerocount = N - onecount
    if onecount == 0 or zerocount == 0:
        print(0)
        return

    __ans = 10**18
    for target in (0, 1):
        

        center = N // 2


        ans = 0
        start = 0
        flip = 0
        i = 0
        f = False
        while i < center:
            while S[i] == target:
                i += 1
                if i >= center:
                    f = True
                    break
            if f:
                break
            
            flip = i
            
            while S[i] != target:
                i += 1
                if i >= center:
                    break
            
            
            ans += i - start + (flip - start)
            # print(start, i, flip, i - start + (flip - start))
            start = i

        start = N - 1
        flip = N - 1
        i = N - 1
        f = False
        while center <= i:
            while S[i] == target:
                i -= 1
                if center > i:
                    f = True
                    break

            if f:
                break
            flip = i

            while S[i] != target:
                i -= 1
                if center > i:
                    break


            ans += start - i + (start - flip)
            # print(start, i, flip, start - i + (start - flip))
            start = i

        __ans = min(__ans, ans)

    print(__ans)


T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    solve(N, [int(c) for c in S])


