import sys

input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]
length.sort(reverse=True)
l, r = 1, max(length)

while l<=r:
    mid = (l+r)//2
    total = 0
    for i in length:
        if i < mid: break
        total += i//mid
        if total >= n: break
    if total >= n:
        l = mid + 1
    else:
        r = mid - 1
print(r)