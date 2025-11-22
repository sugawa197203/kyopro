from math import comb
from itertools import pairwise

def calc(a, b):
    target = min(a, b)
    retval = 0
    for i in range(1, target + 1):
        ac = comb(a, i)
        bc = comb(b, i)
        retval += ac * bc
    return retval

S = input()

ans = 0
l = list(range(10))
for a, b in pairwise(l):
    acount = 0
    bcount = 0
    aindex = 0
    bindex = 0

    while aindex < len(S):
        s_aindex = int(S[aindex])
        if s_aindex == a:
            acount += 1
        elif acount > 0 and s_aindex == b:
            break
        aindex += 1
    
    bindex = aindex
    while bindex < len(S):
        s_bindex = int(S[bindex])
        if s_bindex == b:
            bcount += 1
        elif s_bindex == a:
            break
        bindex += 1

    ans += calc(acount, bcount)
    aindex = bindex
    
    while aindex < len(S):
        acount = 0
        bcount = 0

        while aindex < len(S):
            s_aindex = int(S[aindex])
            if s_aindex == a:
                acount += 1
            elif acount > 0 and s_aindex == b:
                break
            aindex += 1

        while bindex < len(S):
            s_bindex = int(S[bindex])
            if s_bindex == b:
                bcount += 1
            elif s_bindex == a:
                break
            bindex += 1

        ans += calc(acount, bcount)
        aindex = bindex
        bindex += 1
    
print(ans)
