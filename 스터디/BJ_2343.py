import sys

input = sys.stdin.readline

def check(size):
    st, cnt, i = size, 0, 1
    while i<=n:
        if total[i] > st:
            cnt += 1
            if cnt == m: return False
            st = total[i-1] + size
            continue
        i += 1
    return True

n, m = map(int, input().split())
num = list(map(int, input().split()))
total = [0]*(n+1)

for i in range(n):
    total[i+1] = total[i] + num[i]

l, r = total[1], total[n]
while l<r:
    mid = (l+r)//2
    if check(mid): r = mid
    else: l = mid+1
print(l)