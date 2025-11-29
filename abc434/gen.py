N = 2 * 10**5

with open("./output.txt", "w") as f:
    f.write(f"{N}\n")
    for _ in range(N):
        f.write("1 2000 1 2000\n")