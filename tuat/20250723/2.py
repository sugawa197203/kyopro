from itertools import product
A, B, C, D = map(int, list(input()))

op = ["+", "-"]

for ops in product(op, repeat=3):
    if eval(f"{A}{ops[0]}{B}{ops[1]}{C}{ops[2]}{D}") == 7:
        print(f"{A}{ops[0]}{B}{ops[1]}{C}{ops[2]}{D}=7")
        break
