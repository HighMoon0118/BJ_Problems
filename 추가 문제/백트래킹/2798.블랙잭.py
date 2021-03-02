import sys

def makeIt(s, c, total):
    global ans
    if total>m: return
    if c==3:
        ans = max(ans, total)
        return
    for i in range(s, n):
        makeIt(i+1, c+1, total+num[i])


input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
ans = 0
makeIt(0, 0, 0)
print(ans)