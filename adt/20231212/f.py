N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

Scount = sum(row.count('#') for row in S)
Tcount = sum(row.count('#') for row in T)

if Scount != Tcount:
    print("No")
    exit()

SS = []

S_top = 0
for i in range(N):
    if '#' in S[i]:
        S_top = i
        break
S_bottom = 0
for i in range(N - 1, -1, -1):
    if '#' in S[i]:
        S_bottom = i
        break
S_left = 0
for j in range(N):
    if any(S[i][j] == '#' for i in range(N)):
        S_left = j
        break
S_right = 0
for j in range(N - 1, -1, -1):
    if any(S[i][j] == '#' for i in range(N)):
        S_right = j
        break

T_top = 0
for i in range(N):
    if '#' in T[i]:
        T_top = i
        break
T_bottom = 0
for i in range(N - 1, -1, -1):
    if '#' in T[i]:
        T_bottom = i
        break
T_left = 0
for j in range(N):
    if any(T[i][j] == '#' for i in range(N)):
        T_left = j
        break
T_right = 0
for j in range(N - 1, -1, -1):  
    if any(T[i][j] == '#' for i in range(N)):
        T_right = j
        break

S_height = S_bottom - S_top + 1
S_width = S_right - S_left + 1
T_height = T_bottom - T_top + 1
T_width = T_right - T_left + 1

if (S_height != T_height or S_width != T_width) and (S_height != T_width or S_width != T_height):
    print("No")
    exit()

S_cropped = [row[S_left:S_right + 1] for row in S[S_top:S_bottom + 1]]
T_cropped = [row[T_left:T_right + 1] for row in T[T_top:T_bottom + 1]]

import numpy as np

S_array = np.array(S_cropped)
T_array = np.array(T_cropped)

for _ in range(4):
    if np.array_equal(S_array, T_array):
        print("Yes")
        exit()
    S_array = np.rot90(S_array)

print("No")
