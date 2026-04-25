from collections import Counter
N = int(input())
S = input()

accABC = [(0, 0, 0)]
for s in S:
    a, b, c = accABC[-1]
    if s == 'A':
        a += 1
    elif s == 'B':
        b += 1
    else:
        c += 1
    accABC.append((a, b, c))

diff = [(0, 0)]
count = 0
for a, b, c in accABC[1:]:
    diff.append((a - b, a - c))
    if a == b or a == c or b == c:
        count += 1
print(count)
diff_counter = Counter(diff)
same_count = 0

for count in diff_counter.values():
    same_count += count * (count - 1) // 2

total = N * (N + 1) // 2
print(total - same_count)

print(f"total: {total}, same_count: {same_count}")
print(f"diff_counter: {diff_counter}")
print(f"diff: {diff}")
print(f"accABC: {accABC}")
