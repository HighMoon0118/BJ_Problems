import sys
sys.setrecursionlimit(100000)
def make_it(cnt):
    if cnt == 0: return 0

    if dp[cnt]>=0: return dp[cnt]

    result = 0
    for i in range(1, cnt+1):
        result = max(result, cost[i] + make_it(cnt-i))
    dp[cnt] = result
    return result

n = int(input())

cost = [0] + list(map(int, input().split()))
dp = [-1]*(n+1)
print(make_it(n))

# import sys
# sys.setrecursionlimit(100000)
# def make_it(index, cnt):

#     if index > n: return 0

#     if dp[index][cnt]>=0: return dp[index][cnt]

#     result = make_it(index+1, cnt)
#     count = cnt+index
#     plus = cost[index]
#     while count <= n:
#         result = max(result, plus + make_it(index+1, count))
#         count += index
#         plus += cost[index]
#     dp[index][cnt] = result
#     return result
    

# n = int(input())

# cost = [0] + list(map(int, input().split()))
# dp = [[-1]*(n+1) for _ in range(n+1)]
# print(make_it(1, 0))