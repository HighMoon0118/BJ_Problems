import sys

input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
height.sort(reverse=True)

l, r = 1, max(height)
while l<=r:
    mid = (l+r)//2

    total = 0
    for h in height:
        if h<mid: break
        total += (h-mid)
        if total >= m: break
        
    if total >= m:
        l = mid+1
    else:
        r = mid-1
print(r)