import sys
sys.setrecursionlimit(10000)
diff = [(1, 2), (0, 2), (0, 1)]
def make_it(index, color):
    if index==n:
        return 0
    
    if dp[index][color]: return dp[index][color]
    dp[index][color] = cost[index][color] + min(make_it(index+1, diff[color][0]), make_it(index+1, diff[color][1]))

    return dp[index][color]

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
print(min(make_it(0,0), make_it(0,1), make_it(0,2)))