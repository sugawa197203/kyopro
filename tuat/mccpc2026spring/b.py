N = int(input())
S = input()

from collections import Counter

c = Counter(S)

if "M" in c and "C" in c and c["M"] >= 1 and c["C"] >= 2:
    print("Yes")
else:
    print("No")
    