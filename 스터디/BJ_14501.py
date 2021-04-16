import sys

input = sys.stdin.readline

def make_it(next):

    if dp[next] >= 0: return dp[next]

    dp[next] = 0

    for i in range(next+1, n+1):
        if task[i][0] <= n:
            dp[next] = max(dp[next], task[i][1] + make_it(task[i][0]))
    return dp[next]

n = int(input())
task = [[]]+[list(map(int, input().split())) for i in range(n)]
dp = [-1 for _ in range(n+1)]

for i in range(1, n+1): 
    task[i][0] = i + task[i][0] - 1

print(make_it(0))