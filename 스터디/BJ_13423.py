import sys

input = sys.stdin.readline

t = int(input())
ans = []

for _ in range(t):
    n = int(input())
    num = list(map(int, input().split()))
    num.sort()
    cnt = 0
    for i in range(1, n-1):
        l, r = 0, n-1
        while l<r:
            gap = num[l]+num[r]-num[i]*2
            if gap == 0:
                cnt += 1
                l += 1; r -= 1
            elif gap>0:
                r -= 1
            else:
                l += 1
    ans.append(str(cnt))
print("\n".join(ans))

# for _ in range(t):
#     n = int(input())
#     num = list(map(int, input().split()))
#     num.sort()
#     cnt = 0
#     for i in range(n):
#         for j in range(i+2, n):
#             l, r = i+1, j-1
#             while l<=r:
#                 mid = (l+r)//2
#                 if num[mid]-num[i] <= num[j]-num[mid]:
#                     l = mid+1
#                 else:
#                     r = mid-1
#             if num[r]-num[i] == num[j]-num[r]:
#                 cnt += 1
#     ans.append(str(cnt))
# print("\n".join(ans))
