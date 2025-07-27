N, L, R = map(int, input().split())
S = input()

sub = S[L-1:R]
print("Yes" if "o" * len(sub) == sub else "No")
