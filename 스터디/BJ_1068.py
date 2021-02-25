import sys

def dfs(i):
    if not len(tree[i]):
        return 1
    result = 0
    for j in tree[i]:
        result += dfs(j)
            
    return result

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
tree = [[] for _ in range(n)]
for i in range(n):
    if p[i]==-1:
        start = i
    else:
        tree[p[i]].append(i)
delete = int(input())
if delete == start:
    print(0)
else:
    tree[p[delete]].remove(delete)
    print(dfs(start))