import sys

input = sys.stdin.readline

def bellman():
    
    takes = [INF for _ in range(n+1)]
    takes[1] = 0
    for _ in range(n-1):
        for s, e, t in edges:
            if takes[s]+t < takes[e]:
                takes[e] = takes[s]+t
    
    for s, e, t in edges:
        if takes[s]+t < takes[e]:
            return True
    return False

tc = int(input())
INF = 0xfffffff
ans = []

for _ in range(tc):

    n, m, w = map(int, input().split())
    edges = []

    for i in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))

    if bellman(): ans.append("YES")
    else: ans.append("NO")
print("\n".join(ans))