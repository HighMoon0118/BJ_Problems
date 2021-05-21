import sys

input = sys.stdin.readline

def find(a):
    if a == uf[a]:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa, bb = find(a), find(b)
    if aa > bb:
        uf[a] = bb
    else:
        uf[b] = aa


n, m = map(int, input().split())
god = [(-1,-1)]
uf = [0]*(n+1)

for i in range(1, n+1):
    god.append(tuple(map(int, input().split())))
    uf[i] = i

for _ in range(m):
    a, b = map(int, input().split())
    union(find(a), find(b))

dist = [(((god[i][0]-god[j][0])**2 + (god[i][1]-god[j][1])**2)**0.5,i,j) for i in range(1, n) for j in range(i+1, n+1)]
dist.sort(key=lambda x : x[0])

ans = 0
for d, i, j in dist:
    if find(i) != find(j):
        union(uf[i], uf[j])
        ans += d

print("{:.2f}".format(ans))