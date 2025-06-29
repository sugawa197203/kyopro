from itertools import product

def check(kakko):
    stack = 0
    for k in kakko:
        if k == "(":
            stack += 1
            continue
        if stack == 0:
            return False
        stack -= 1
    return stack == 0

N = int(input())
if N % 2 == 1:
    exit()

for kakko in product(("(", ")"), repeat=N):
    if check(kakko):
        print("".join(kakko))

