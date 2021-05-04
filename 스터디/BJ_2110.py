import sys

input = sys.stdin.readline

def check():
    st = home[0] + mid
    i = cnt = 1
    while i<n:
        if home[i] >= st:
            cnt += 1
            if cnt == c: return True
            st = home[i] + mid
        i += 1
    return False

n, c = map(int, input().split())
home = [int(input()) for _ in range(n)]
home.sort()
l, r = 1, home[-1]

while l<r:
    mid = (l+r)//2
    if check(): l = mid+1
    else: r = mid
print(l-1)