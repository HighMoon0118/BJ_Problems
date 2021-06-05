import sys
input = sys.stdin.readline

def makeIt(parent, child, flag):

    if dp[child][flag]: return dp[child][flag]

    if flag:
        result = [child]
        for i in link[child]:
            if i != parent:
                result += makeIt(child, i, 0)
        dp[child][flag] = result
        return result
        
    result = []
    for i in link[child]:
        if i != parent:
            a = makeIt(child, i, 1)
            b = makeIt(child, i, 0)
            if sum([w[i] for i in a]) > sum([w[i] for i in b]): 
                result += a
            else: result += b
    dp[child][flag] = result
    return result

n = int(input())
w = [0]+list(map(int,input().split()))

link = [[] for _ in range(n+1)]

while True:
    line = input().strip()
    if not line: break

    a, b = map(int, line.split())
    link[a].append(b)
    link[b].append(a)

dp = [[[] for _ in range(2)] for _ in range(n+1)]
link[0].append(1)

ans = makeIt(0, 0, 0)
ans.sort()
print(sum([w[i] for i in ans]))
print(*ans)