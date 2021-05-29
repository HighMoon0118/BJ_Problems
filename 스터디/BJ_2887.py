import sys

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa > bb: uf[a] = bb
    else: uf[b] = aa

input = sys.stdin.readline

n = int(input())

dot = [list(map(int, input().split()))+[i] for i in range(n)]
uf = [i for i in range(n)]

dot.sort(key=lambda x: x[0])

link = []
for i in range(n-1):
    link.append((dot[i+1][0]-dot[i][0], dot[i][3], dot[i+1][3]))
dot.sort(key=lambda x: x[1])
for i in range(n-1):
    link.append((dot[i+1][1]-dot[i][1], dot[i][3], dot[i+1][3]))
dot.sort(key=lambda x: x[2])
for i in range(n-1):
    link.append((dot[i+1][2]-dot[i][2], dot[i][3], dot[i+1][3]))

cnt = 0
ans = 0
link.sort(key=lambda x: x[0])
for d, a, b in link:
    if find(a) != find(b):
        union(uf[a], uf[b])
        ans += d
        cnt += 1
        if cnt == n-1: break

print(ans)