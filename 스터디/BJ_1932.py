def make_it(row, col):
    if row == n:
        return 0

    if dp[row][col]: return dp[row][col]

    dp[row][col] = tree[row][col] + max(make_it(row+1, col), make_it(row+1, col+1))
    
    return dp[row][col]

n = int(input())
tree = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(i+1) for i in range(n)]
print(make_it(0, 0))