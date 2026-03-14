L, R, D, U = map(int, input().split())

maxsize = max(abs(L), abs(R), abs(D), abs(U))
ans = 0

for i in range(maxsize + 1):
    if i % 2 == 1:
        continue

    blackwhiteX = max(0, min(R, i) - max(L, -i) + 1)
    blackwhiteY = max(0, min(U, i) - max(D, -i) + 1)
    blackwhite = blackwhiteX * blackwhiteY

    whiteonlyX = max(0, min(R, i - 1) - max(L, -i + 1) + 1)
    whiteonlyY = max(0, min(U, i - 1) - max(D, -i + 1) + 1)
    whiteonly = whiteonlyX * whiteonlyY


    ans += blackwhite - whiteonly
    # print(f'i={i}, blackwhiteX={blackwhiteX}, blackwhiteY={blackwhiteY}, blackwhite={blackwhite}, whiteonlyX={whiteonlyX}, whiteonlyY={whiteonlyY}, whiteonly={whiteonly}, ans={ans}')


print(ans)
