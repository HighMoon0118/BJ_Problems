import sys

input = sys.stdin.readline

n, height = map(int, input().split())

col = [int(input()) for _ in range(n)]
a = col[0:n:2]
b = col[1:n:2]

a.sort()
b.sort(reverse=True)

cnt = len(a)
i, j = 0, 0
ans = n
ansCnt = 1
for h in range(1, height+1):

    while i<len(a):
        if a[i] < h:
            cnt -= 1
            i += 1
        else: break

    h = height-h
    while j<len(b):
        if b[j] > h:
            cnt += 1
            j += 1
        else: break
    if ans < cnt: continue
    elif ans == cnt:
        ansCnt += 1
    else:
        ans = cnt
        ansCnt = 1
print(ans, ansCnt)