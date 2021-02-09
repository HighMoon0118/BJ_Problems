import sys

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
ans = 0
for i in range(n):
    start = i
    up = 0
    while start<n-1:
        if h[start]<h[start+1]:
            up = h[start+1] - h[i]
            start+=1
        else:
            break
    ans = max(ans, up)

print(ans)