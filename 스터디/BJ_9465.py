import sys
t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    board = [[0]+list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*(n+1) for _ in range(3)]

    for i in range(1, n+1):
        dp[0][i] = board[0][i] + max(dp[1][i-1], dp[2][i-1])
        dp[1][i] = board[1][i] + max(dp[0][i-1], dp[2][i-1])
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])

    ans.append(str(max(dp[0][n],dp[1][n],dp[2][n])))
print("\n".join(ans))
# import sys
# sys.setrecursionlimit(200000)

# input = sys.stdin.readline

# def make_it(row, col):
#     if col == n: return 0

#     if dp[row][col]: return dp[row][col]

#     result = 0
#     if row == 1:
#         result = max(result, board[0][col] + make_it(0, col+1))
#     elif row == 0:
#         result = max(result, board[1][col] + make_it(1, col+1))
#     else:
#         result = max(result, board[0][col] + make_it(0, col+1), board[1][col] + make_it(1, col+1))

#     dp[row][col] = max(result, make_it(2, col+1))

#     return dp[row][col]

# t = int(input())
# ans = []

# for _ in range(t):
#     n = int(input())
#     board = [list(map(int, input().split())) for _ in range(2)]
#     dp = [[0]*n for _ in range(3)]
#     ans.append(str(make_it(2, 0)))
# print("\n".join(ans))