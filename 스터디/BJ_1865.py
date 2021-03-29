import sys

input = sys.stdin.readline

def bellman():  
    # 시작지점으로부터 최단거리를 구하는 것이 아니라
    # 사이클의 여부만 판단하는 문제이기 때문에 시작지점과의 연결여부가 필요 없다
    
    takes = [INF for _ in range(n+1)]
    for _ in range(n-1):
        for s, e, t in edges:
            if takes[s]+t < takes[e]:  # 시작지점과의 연결여부를 묻는 코드가 빠짐
                takes[e] = takes[s]+t
    
    for s, e, t in edges:
        if takes[s]+t < takes[e]:
            return True
    return False

tc = int(input())
INF = 0xfffffff

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

    if bellman(): print("YES")
    else: print("NO")