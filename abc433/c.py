S = input()

start = 0
center = 0
end = 0

ans = 0

while center < len(S) - 1:
    if S[center] == S[center + 1]:
        center += 1
    else:
        break

if center == len(S) - 1:
    print("0")
    exit()
    
end = center + 1
while end < len(S) - 1:
    if S[end] == S[end + 1]:
        end += 1
    else:
        break

while center < len(S) - 1:

    if int(S[end]) - int(S[start]) == 1:
        leftcount = center - start + 1
        rightcount = end - center
        ans += min(leftcount, rightcount)

    start = center + 1
    center = end
    
    end += 1
    while end < len(S) - 1:
        if S[end] == S[end + 1]:
            end += 1
        else:
            break


print(ans)
