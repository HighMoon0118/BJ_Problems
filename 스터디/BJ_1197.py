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

v, e = map(int, input().split())
uf = [i for i in range(v+1)]
link = [tuple(map(int, input().split())) for _ in range(e)]
link.sort(key=lambda x:x[2])

ans = 0
cnt = 0
for a, b, c in link:
    if find(a) != find(b):
        union(uf[a], uf[b])
        ans += c
        cnt += 1
        if cnt==v-1: break
print(ans)