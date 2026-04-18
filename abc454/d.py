
T = int(input())

def remove_kakko(s: str) -> str:
    N = len(s)
    stack = 0
    xcount = 0
    retval = ""
    for i in range(N):
        # print(f"i: {i}, s[i]: {s[i]}, stack: {stack}, xcount: {xcount}, retval: {retval}")
        if s[i] == '(':
            if xcount == 0:
                stack += 1
                continue
            if xcount > 0:
                retval += '(' * stack + 'x' * xcount
                stack = 1
                xcount = 0
                continue
            stack += 1
            continue
        if s[i] == ')':
            if xcount == 2:
                stack -= 1
                if stack == 0:
                    retval += 'xx'
                    xcount = 0
                continue
            if stack == 0:
                retval += 'x' * xcount + ')'
            else:
                retval += '(' * stack + 'x' * xcount + ')' * stack
                stack = 0
            xcount = 0
            continue
        if s[i] == 'x':
            if stack == 0:
                retval += 'x'
                continue
            if xcount == 2:
                retval += '(' * stack
                stack = 0
                xcount = 0
                retval += 'xxx'
                continue
            xcount += 1
            continue
    retval += '(' * stack + 'x' * xcount
    return retval

def solve(A:str, B:str) -> bool:
    # print("-" * 20)
    _A = remove_kakko(A)
    _B = remove_kakko(B)
    # print(f"_A: {_A}, _B: {_B}")
    return _A == _B or A == B

for _ in range(T):
    A = input()
    B = input()
    print("Yes" if solve(A, B) else "No")
