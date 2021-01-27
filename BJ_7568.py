import sys

input = sys.stdin.readline

n = int(input())
info = []
for i in range(n) :
    w, t = map(int, input().split())
    info.append((i, w, t))

info.sort(key=lambda x : x[1])
ans = [1 for _ in range(n)]
for i in range(n) :
    count = 0
    for j in range(i+1, n) :
        if info[i][2]<info[j][2] :
            count+=1
    ans[info[i][0]]+=count

print(*ans)