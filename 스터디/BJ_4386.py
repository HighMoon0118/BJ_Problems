import sys

input = sys.stdin.readline

def find(a):
    if a==uf[a]:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa, bb = find(a), find(b)
    if aa > bb:
        uf[a] = bb
    else:
        uf[b] = aa

n = int(input())
uf = [i for i in range(n+1)]

star = [(-1,-1)]+[tuple(map(float,input().split())) for _ in range(n)]
dist = [(((star[i][0]-star[j][0])**2 + (star[i][1]-star[j][1])**2)**0.5,i,j) for i in range(1, n) for j in range(i+1, n+1)]
dist.sort(key=lambda x:x[0])

ans = 0
for d, i, j in dist:
    if find(i) != find(j):
        union(uf[i], uf[j])
        ans += d

print("{:.2f}".format(ans))