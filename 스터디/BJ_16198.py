import sys

input = sys.stdin.readline

def makeIt(s):
    global ans
    if linked[n-1][0] == 0:
        if ans < s:
            ans = s
        return
    for i in range(1, n-1):
        if not used[i]:
            used[i] = True
            linked[linked[i][0]][1] = linked[i][1]
            linked[linked[i][1]][0] = linked[i][0]
            makeIt(s + w[linked[i][0]]*w[linked[i][1]])
            used[i] = False
            linked[linked[i][0]][1] = i
            linked[linked[i][1]][0] = i

n = int(input())
w = list(map(int, input().split()))
used = [False for _ in range(n)]
linked = [[i-1, i+1] for i in range(n)]
ans = 0
makeIt(0)
print(ans)