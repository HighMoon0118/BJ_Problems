import sys

input = sys.stdin.readline
ans = []

def dfs(parent, node):
    global is_tree
    visited[node] = cnt
    for i in tree[node]:
        if i != parent and visited[i] == visited[node]:
            is_tree = False
        elif not visited[i]:
            dfs(node, i)
c = 1

while True:
    n, m = map(int, input().split())
    if n == 0: break

    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    visited = [0]*(n+1)
    cnt = 0
    is_tree = True
    tree_cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            cnt += 1
            dfs(0, i)
            if is_tree:
                tree_cnt += 1
            is_tree = True
            
    
    if tree_cnt>1:
        ans.append(f'Case {c}: A forest of {tree_cnt} trees.')
    elif tree_cnt==1:
        ans.append(f'Case {c}: There is one tree.')
    else:
        ans.append(f'Case {c}: No trees.')
    c += 1

print('\n'.join(ans))