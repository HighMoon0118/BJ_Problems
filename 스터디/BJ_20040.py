import sys

input = sys.stdin.readline

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(uf[a])
    bb = find(uf[b])
    if aa > bb: uf[aa] = bb
    else: uf[bb] = aa

n, m = map(int, input().split())
uf = [i for i in range(n)]
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if find(a)!=find(b):
        union(a, b)
    elif ans == 0:
        ans = i+1
        break
print(ans)