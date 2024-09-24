import itertools

def is_k_length_palindrome(s, K):
    for i in range(len(s) - K + 1):
        substring = s[i:i + K]
        if substring == substring[::-1]:
            return True
    return False

N, K = map(int, input().split())
S = list(input())

unique_permutations = set(itertools.permutations(S))
count = 0

for perm in unique_permutations:
    if not is_k_length_palindrome(perm, K):
        count += 1

print(count)
