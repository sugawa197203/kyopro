N = int(input())

SS = input().split()

d = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz"
]

ans = ""

for s in SS:
    top = s[0]
    for i, _d in enumerate(d):
        if top in _d:
            ans += str(i + 2)
            break

print(ans)    
