import sys
from collections import deque

input = sys.stdin.readline

c = int(input())
ans = []

for _ in range(c) :
    n = int(input())
    sR, sC = map(int, input().split())
    eR, eC = map(int, input().split())

    dR = 1, 2, 2, 1, -1, -2, -2, -1
    dC = 2, 1, -1, -2, -2, -1, 1, 2
    visited = [[ 0 for _ in range(n)] for _ in range(n)]
    que = deque()
    que.append((sR, sC, 0))
    visited[sR][sC]=1
    while que :
        r, c, count = que.popleft()
        if r==eR and c==eC : break
        for i in range(8) :
            nR, nC = r+dR[i], c+dC[i]
            if 0<=nR<n and 0<=nC<n and not visited[nR][nC] :
                visited[nR][nC] = 1
                que.append((nR,nC,count+1))
    ans.append(count)

print('\n'.join(map(str, ans)))