import sys

input = sys.stdin.readline

n, k = map(int, input().split())

nation = []
for i in range(n):
    nation.append(list(map(int, input().split())))
    if nation[i][0]==k:
        target = nation[i]
rank = 1
for next in nation:
    for i in range(1,4):
        if next[i]>target[i]:
            rank+=1
            break
        elif next[i]<target[i]:
            break
print(rank)