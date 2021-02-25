import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def dfs(i):
    for next in tree[i]:
        if not visited[next]:
            visited[next] = 1
            p[next] = i
            dfs(next)

n = int(input())
tree = [[] for _ in range(n+1)]  # 트리
visited = [0 for _ in range(n+1)]  # 방문 여부
p = [[] for _ in range(n+1)]  # 부모 노드 저장

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited[1] = 1
dfs(1)
print("\n".join(map(str, p[2:])))