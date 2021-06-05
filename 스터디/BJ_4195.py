import sys
input = sys.stdin.readline

def find(a):
    if uf[a]==a: return a
    uf[a] = find(uf[a])
    return uf[a]

def union(a, b):
    aa = find(uf[a])
    bb = find(uf[b])
    if aa > bb:
        uf[aa] = bb
        cnt[bb] += cnt[aa]
    elif aa < bb:
        uf[bb] = aa
        cnt[aa] += cnt[bb]

tc = int(input())
ans = []
for _ in range(tc):
    f = int(input())
    toNum = {}
    link = []
    idx = 0
    for _ in range(f):
        link.append(tuple(input().split()))
        if link[-1][0] not in toNum:
            toNum[link[-1][0]] = idx
            idx += 1
        if link[-1][1] not in toNum:
            toNum[link[-1][1]] = idx
            idx += 1

    cnt = [1]*(idx)
    uf = [i for i in range(idx)]
    for a, b in link:
        a = toNum[a]
        b = toNum[b]
        if find(a) != find(b):
            union(uf[a], uf[b])
        ans.append(str(cnt[find(a)]))

    
print("\n".join(ans))