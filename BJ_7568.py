import sys

input = sys.stdin.readline

n = int(input())
info = []
for i in range(n) :
    w, t = map(int, input().split())
    info.append((w, t, i))

info.sort()
ans = [1 for _ in range(n)]
for i in range(n) :
    count = 0
    for j in range(i+1, n) :
        if info[i][1]<info[j][1] and info[i][0]!=info[j][0] :
            count+=1
    ans[info[i][2]]+=count

print(*ans)