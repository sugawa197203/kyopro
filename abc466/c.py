N = int(input())


def nC2(n):
    return n * (n - 1) // 2


if N == 2:
    print("? 1 2")
    print("! 1" if input() == "Yes" else "! 0")
    exit()

right = 2
left = 1
ans = 0


def q(a, b):
    print(f"? {a} {b}")
    return input() == "Yes"


while left != N and right <= N:
    # print(f"{ans=}, {left=}, {right=}")

    if q(left, right):
        ans += 1
        right += 1
        continue
    left += 1
    if left == right:
        right += 1
        continue

    if left != N:
        ans += right - left - 1

right -= 1
while left < N:
    ans += right - left - 1
    left += 1
# print(f"{ans=}, {left=}, {right=}")
print(f"! {ans}")
