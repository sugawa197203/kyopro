S = input()

from itertools import groupby, product


def real(_S):
    l = len(_S)
    count = 0
    for start in range(l):
        for end in range(start, l):
            _s = _S[start:end + 1]
            print(_s)
            for i in range(len(_s) - 1):
                if _s[i] == _s[i + 1]:
                    break
            else:
                count += 1
    return count

def generate(n):
    for i in range(1, n + 1):
        for c in product("abc", repeat=i):
            yield "".join(c)

def solve(S):
    count = 0
    ans = 0

    g = groupby(S)

    for k, g in groupby(S):
        length = len(list(g))
        if length == 1:
            count += 1
            continue

        count += 1
        ans += count * (count + 1) // 2
        ans += length - 2

        count = 1
    
    ans += count * (count + 1) // 2
    return ans

print(solve(S) % 998244353)
# print(real(S))

# for s in generate(10):
#     if real(s) != solve(s):
#         print(s)
#         break
