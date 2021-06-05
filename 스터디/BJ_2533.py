import sys
sys.setrecursionlimit(2000000)
input = sys.stdin.readline

def makeIt(parent, child, flag):

    if dp[child][flag] >= 0: return dp[child][flag]

    if flag:
        result = 1
        for i in link[child]:
            if i != parent:
                result += min(makeIt(child, i, 1), makeIt(child, i, 0))
        dp[child][flag] = result
        return result
    
    result = 0
    for i in link[child]:
        if i != parent:
            result += makeIt(child, i, 1)
    dp[child][flag] = result
    return result

n = int(input())
link = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

dp = [[-1]*2 for _ in range(n+1)]
link[0].append(1)
makeIt(0,0,1)
print(min(dp[1][0], dp[1][1]))