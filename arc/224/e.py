from sortedcontainers import SortedList


def get3(ss, last):
    return ss[last - 2 : last + 1]


def solve(S: str) -> int:
    SS = SortedList()
    for i, c in enumerate(S):
        SS.add((i, c))

    index = len(S) - 1

    while len(SS) >= 3 and index >= 2:
        if index >= len(SS):
            index = len(SS) - 1
        ithree = get3(SS, index)
        three = "".join(c for _, c in ithree)
        # print(f"{ithree=}, {index=}, {SS=}")
        if three == "AAA":
            SS.remove(ithree[0])
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "AAB":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "AAC":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ABA":
            SS.remove(ithree[0])
            SS.remove(ithree[1])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ABB":
            SS.remove(ithree[0])
            SS.remove(ithree[1])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ABC":
            SS.remove(ithree[0])
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ACA":
            SS.remove(ithree[0])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ACB":
            SS.remove(ithree[1])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "ACC":
            SS.remove(ithree[0])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BAA":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BAB":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BAC":
            SS.remove(ithree[1])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BBA":
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BBB":
            pass
        elif three == "BBC":
            pass
        elif three == "BCA":
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "BCB":
            pass
        elif three == "BCC":
            pass
        elif three == "CAA":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "CAB":
            SS.remove(ithree[1])
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "CAC":
            SS.remove(ithree[1])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "CBA":
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "CBB":
            pass
        elif three == "CBC":
            pass
        elif three == "CCA":
            SS.remove(ithree[2])
            if index >= len(SS):
                index = len(SS) - 1
            continue
        elif three == "CCB":
            pass
        elif three == "CCC":
            pass

        index -= 1

    if len(SS) == 2:
        s = "".join(c for _, c in SS)
        if s in {"AA", "AB"}:
            return 0
        if s in {"AC", "BA", "CA"}:
            return 1
        else:
            return 2
    if len(SS) == 1:
        s = "".join(c for _, c in SS)
        if s == "A":
            return 0
        else:
            return 1

    return len(SS)


T = int(input())
for _ in range(T):
    S = input()
    print(solve(S))
