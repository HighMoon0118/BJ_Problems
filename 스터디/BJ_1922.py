import sys

input = sys.stdin.readline

def find(a):
    if a == uf[a]:
        return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa < bb: uf[bb] = aa
    else: uf[aa] = bb

n = int(input())
m = int(input())

link = []
for _ in range(m):
    a, b, c = map(int, input().split())
    link.append((c, a, b))

link.sort(key=lambda x: x[0])

uf = [i for i in range(n+1)]
ans = 0
cnt = 0
for c, a, b in link:
    if find(a) != find(b):
        ans += c
        cnt += 1
        union(a, b)
    if cnt == n-1:
        break

print(ans)