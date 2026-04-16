import sys

def judge(input_file, output_file):
    with open(input_file) as f:
        tokens = f.read().split()
    idx = 0
    N = int(tokens[idx]); idx += 1
    M = int(tokens[idx]); idx += 1
    C = int(tokens[idx]); idx += 1
    desired = []
    for i in range(M):
        desired.append(int(tokens[idx])); idx += 1
    food = {}
    for r in range(N):
        for c in range(N):
            v = int(tokens[idx]); idx += 1
            if v != 0:
                food[(r, c)] = v

    # Initial snake
    body = [(4,0),(3,0),(2,0),(1,0),(0,0)]
    colors = [1,1,1,1,1]

    with open(output_file) as f:
        moves = [line.strip() for line in f if line.strip()]

    dir_map = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}

    T = len(moves)
    for t, m in enumerate(moves):
        dr, dc = dir_map[m]
        hr, hc = body[0]
        nr, nc = hr + dr, hc + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            print(f"Turn {t}: out of bounds")
            return
        if len(body) >= 2 and (nr, nc) == body[1]:
            print(f"Turn {t}: U-turn")
            return

        # Move
        new_body = [(nr, nc)] + body[:-1]
        new_colors = list(colors)

        # Eating
        if (nr, nc) in food:
            fc = food[(nr, nc)]
            del food[(nr, nc)]
            new_body = [(nr, nc)] + body  # keep tail
            new_colors = list(colors) + [fc]
        else:
            # Biting
            hit = -1
            for i in range(1, len(new_body) - 1):
                if new_body[i] == (nr, nc):
                    hit = i
                    break
            if hit != -1:
                for p in range(hit + 1, len(new_body)):
                    food[new_body[p]] = new_colors[p]
                new_body = new_body[:hit + 1]
                new_colors = new_colors[:hit + 1]

        body = new_body
        colors = new_colors

    k = len(body)
    E = 0
    for i in range(min(k, M)):
        if colors[i] != desired[i]:
            E += 1

    score = T + 10000 * (E + 2 * (M - k))
    print(f"T={T}, k={k}, M={M}, E={E}, missing={M-k}, score={score}")

judge(sys.argv[1], sys.argv[2])
