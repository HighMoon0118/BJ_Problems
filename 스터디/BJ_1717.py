import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def find(a):
    if uf[a] == a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(a)
    bb = find(b)
    if aa > bb : uf[aa] = bb
    else: uf[bb] = aa

n, m = map(int, input().split())
uf = [i for i in range(n+1)]
ans = []
for _ in range(m):
    how, a, b = map(int, input().split())
    if how:
        if find(a) == find(b):
            ans.append("YES")
        else: ans.append("NO")
    else:
        union(a, b)
print("\n".join(ans))
