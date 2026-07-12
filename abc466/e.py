N, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]

AdiffB = [B - A for A, B in AB]

erabu, erabanai = [-(10**10)] * (N + 1), [-(10**10)] * (N + 1)
erabu[0] = 0
erabanai[0] = 0

ABcomp = [AdiffB[0]]

for addifb in AdiffB[1:]:
    print(f"{ABcomp=}, {addifb=}")
    if (ABcomp[-1] < 0 and addifb < 0) or (ABcomp[-1] >= 0 and addifb >= 0):
        ABcomp[-1] += addifb
    else:
        ABcomp.append(addifb)

Asum = sum([A for A, B in AB])
ABcompPlusCount = sum([1 for ab in ABcomp if ab > 0])
ABcompUp = sorted(ABcomp, reverse=True)

if ABcompPlusCount <= K:
    ans = Asum + sum(ABcompUp[:ABcompPlusCount])
    print(ans)
    # exit()

ABcompDown = sorted(ABcomp)

print(
    f"ABcomp: {ABcomp}, Asum: {Asum}, AdiffB: {AdiffB}, ABcompPlusCount: {ABcompPlusCount}, ABcompUp: {ABcompUp}, ABcompDown: {ABcompDown}"
)
