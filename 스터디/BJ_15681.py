import sys
sys.setrecursionlimit(200000)

input = sys.stdin.readline

def dfs(node):
    visit[node] = 1
    result = 1
    for i in link[node]:
        if not visit[i]:
            result += dfs(i)
    cnt[node] = result
    return cnt[node]

n, r, q = map(int, input().split())

link = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

cnt = [0]*(n+1)
visit = [0]*(n+1)
dfs(r)
ans = []
for _ in range(q):
    ans.append(str(cnt[int(input())]))
print("\n".join(ans))