import sys
from collections import deque
input = sys.stdin.readline

c = int(input())
ans = []

for _ in range(c) :
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for i in range(m) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    que = deque()
    isBN = True
    teamNum = [-1 for _ in range(n+1)]
    for i in range(1, n+1) : 
        if teamNum[i]==-1 :
            que.append(i)
            teamNum[i]=0
            while que :
                now = que.popleft()
                for next in graph[now] :
                    if teamNum[next]==-1 :
                        teamNum[next]=(teamNum[child]+1)%2
                        que.append(next)
                    elif teamNum[next]!=(teamNum[child]+1)%2 :
                        isBN=False
                        break
                if not isBN : break
        if not isBN : break
    if isBN : ans.append('YES')
    else : ans.append('NO')

print('\n'.join(ans))