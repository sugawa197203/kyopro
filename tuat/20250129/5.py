S = input()
from collections import Counter
from itertools import permutations

hachi = []
n = 0
while n < 1000:
    n += 8
    if str(n).count("0") == 0:
        hachi.append(n)
    
    
if len(S) <= 3:
    for p in permutations(S):
        if int("".join(p)) % 8 == 0:
            print("Yes")
            exit()
    print("No")
    exit()
    
sc = Counter(S)
for i in hachi:
    i = str(i).zfill(3)
    ic = Counter(str(i))
    if ic - sc == Counter():
        _sc = sc.copy()
        for k, v in ic.items():
            _sc[k] -= 1
        for k, v in _sc.items():
            if k != "0" and v < 0:
                break
        print("Yes")
        exit()
print("No")
