import sys
import math

input = sys.stdin.readline

n = int(input())
num_list = []
cnt = {}
for _ in range(n):
    next = int(input())
    num_list.append(next)
    cnt[next] = cnt.get(next, 0)+1

nSum = sum(num_list)
avg = round(nSum/n)

num_list.sort()
mid = num_list[n//2]

sort_cnt = sorted(cnt, key=lambda x : (-cnt[x], x))
max_cnt = sort_cnt[1] if len(cnt)>1 and cnt[sort_cnt[0]]==cnt[sort_cnt[1]] else sort_cnt[0]

gap = num_list[-1]-num_list[0]

print("\n".join(map(str, [avg, mid, max_cnt, gap])))