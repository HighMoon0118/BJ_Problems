import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
l, r = 0, n-1
gap = 2000000000
while l<r:
    mGap = num[l]+num[r]
    
    if mGap==0:
        ans = f'{num[l]} {num[r]}'
        break
    
    if gap > abs(mGap):
        gap = abs(mGap)
        ans = f'{num[l]} {num[r]}'

    if abs(num[l]) > abs(num[r]):
        l += 1
    else:
        r -= 1
print(ans)