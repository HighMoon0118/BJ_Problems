import sys

input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
while True:
    w, h = map(int, input().split())
    if w==0 and h==0: break

    G = [[0 for _ in range(w)] for _ in range(h)]

    g = int(input())
    for _ in range(g):
        c, r = map(int, input().split())
        G[r][c] = 1

    e = int(input())
    E = [[0 for _ in range(w)] for _ in range(h)]
    link = []
    for _ in range(e):
        c1, r1, c2, r2, t = map(int, input().split())
        E[r1][c1] = 1
        link.append((c1, r1, c2, r2, t))

    for r in range(h):
        for c in range(w):
            if E[r][c] or G[r][c] or (r==h-1 and c==w-1): continue
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if 0<= nr < h and 0<= nc < w and not G[nr][nc]:
                    link.append((c, r, nc, nr, 1))

    MAX = 1000000000000
    time = [[MAX for _ in range(w)] for _ in range(h)]
    time[0][0] = 0
    n = w*h
    n_cycle = False

    for i in range(n-1):
        for c1, r1, c2, r2, t in link:
            if time[r1][c1] != MAX and time[r2][c2] > time[r1][c1] + t:
                time[r2][c2] = time[r1][c1] + t
    for c1, r1, c2, r2, t in link:
        if time[r1][c1] != MAX and time[r2][c2] > time[r1][c1] + t:
            n_cycle =  True
            break
    if n_cycle: print("Never")
    elif time[h-1][w-1]==MAX: print("Impossible")
    else: print(str(time[h-1][w-1]))