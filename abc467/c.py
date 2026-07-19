from copy import deepcopy

N, M = map(int, input().split())
Aorigin = list(map(int, input().split()))
Borigin = list(map(int, input().split()))
# Aorigin = deepcopy(A)
ans = []


for r in [True, False]:
    for f in [1, 2]:
        _ans = 0
        A = deepcopy(Aorigin)
        B = deepcopy(Borigin)
        if r:
            A.reverse()
            B.reverse()

        if f == 1:
            A[0] += 1
            _ans += 1
        for i in range(N - 1):
            # print(f"{A=}, {B=}, {i=}")
            if (A[i] + A[i + 1]) % 2 != B[i]:
                _ans += 1
                A[i + 1] += 1
        ans.append(_ans)
        # print(f"{ans=}, {A=}, {B=}, {_ans=}")

    # print("=========")
    A = deepcopy(Aorigin)
    B = deepcopy(Borigin)
    if r:
        A.reverse()
        B.reverse()
    _ans = 0
    for i in range(N - 1):
        # print(f"{A=}, {B=}, {i=}")
        if (A[i] + A[i + 1]) % 2 != B[i]:
            _ans += 1
            A[i + 1] += 1
    ans.append(_ans)
    # print(f"{ans1=}, {ans2=}")
    # print(f"{A=}, {_A=}")

# print(f"{ans=}, {A=}, {B=}, {_ans=}")
print(min(ans))
