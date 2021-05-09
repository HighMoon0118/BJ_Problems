import sys

input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))

time.sort()
l, r = 1, time[0]*m
ans = r
while l<=r:
    mid = (l+r)//2
    cnt = 0
    for i in range(n):
        if time[i]>mid or cnt > m:
            break
        cnt += mid//time[i]
    if cnt >= m:
        r = mid - 1
    else:
        l = mid + 1
print(l)