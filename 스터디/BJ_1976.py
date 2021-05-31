import sys

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

n = int(input())
m = int(input())

uf = [i for i in range(n)]

table = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        if table[i][j]:
            union(i, j)

city = tuple(map(int, input().split()))

for i in range(m-1):
    if find(city[i]-1)!=find(city[i+1]-1):
        print("NO")
        break
else:
    print("YES")