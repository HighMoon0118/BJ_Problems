# 다시 풀어 보고싶은 문제들



### 7576번 문제 : 토마토

> 나는 BFS, DFS는 자신있다고 생각했었는데 나에게 충격을 줬던 문제이다.
>
> 보통 BFS는 큐로 구현을 하게 되고
>
> 어떤 노드를 큐 안에 넣을 땐 방문을 했다고 기록을하고 넣어야 한다.
>
> 하지만 나는 큐에서 꺼내고 나서 방문 기록을 체크했다.
>
> 이렇게하게 되면 큐안에 같은 노드가 여러번 들어갈 뿐만 아니라
>
> 최단거리를 구하는 문제라면 틀린답이 나오게 된다.
>
> **<옳은 풀이>**

```python
while que :
    
    r,c,count = que.popleft()
    
    for i in range(4) :
        nextR, nextC = r+dr[i], c+dc[i]
        if 0<=nextR and 0<=nextC and board[nextR][nextC]==0 :
            board[nextR][nextC]=1  # 큐 안에 넣기 전에 기록
            ans = count+1
            que.append((nextR, nextC, ans))
```

**<틀린 풀이>**

```python
while que :
    
    r,c,count = que.popleft()
    board[r][c]=1  # 큐에서 꺼내고 나서 기록
    
    for i in range(4) :
        nextR, nextC = r+dr[i], c+dc[i]
        if 0<=nextR and 0<=nextC and board[nextR][nextC]==0 :
            que.append((nextR, nextC, count+1))
```



### 1623번 문제 : 아기 상어

> 파이썬으로 처음으로 우선순위 큐를 사용해봤다.
>
> Comparator나 Comparable을 사용하는 자바와 다르게
>
> 정렬기준의 값을 넣고 오름차순 정렬을 한다는 느낌을 받았다.

```python
from queue import PriorityQueue

def findFish(r, c, s) :
    que = PriorityQueue()  # 우선순위 큐
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c]=True
    que.put((0,r,c))  # 인덱스의 값을 비교하며 오름차순 정렬
    while not que.empty() :
        d, row, col = que.get()
        if 0<board[row][col]<s : 
            return d, row, col
        for i in range(4) :
            nr, nc = row+dr[i], col+dc[i]
            if 0<=nr<n and 0<=nc<n and not visited[nr][nc] :
                visited[nr][nc] = True
                if board[nr][nc]<=s :
                    que.put((d+1, nr, nc))

    return 0, 0, 0
```



### 1707번 문제 : 이분 그래프

> 그래프의 정점들을 두 집합으로 분할하고, 각 집합에 속한 정점끼리는 서로 인접하지 않는 것을 **이분 그래프**라 부른다.
>
> 처음 이 문제를 순환이 있는지 없는지로 풀었는데 틀린 답이 나왔다.
>
> 간선이 1-2, 2-3, 3-4, 4-1 로 주어질 경우, 1에서 시작해서 1로 돌아오지만 이분 그래프는 될 수 있는 반례가 있기 때문이다. (1,3이 같은집합, 2,4가 같은 집합)
>
> 그 다음엔, 집합은 두개 밖에 없기 때문에 각 집합에 0과 1이라는 숫자를 부여했고, 각 노드마다 속한 집합의 번호를 기록하며 문제를 풀어나갔다.

```python
que = deque()
isBN = True
teamNum = [-1 for _ in range(n+1)]
for i in range(1, n+1) :  # 모든 노드를 조사
    if teamNum[i]==-1 :
        que.append(i)
        teamNum[i]=0  # 시작 노드의 집합 번호를 0으로 지정
        while que :
            now = que.popleft()
                for next in graph[now] :
                if teamNum[next]==-1 :  
                    # 아직 집합 번호가 없다면 이전 노드와 다른 집합 번호 부여
                    teamNum[next]=(teamNum[now]+1)%2
                    que.append(next)
                elif teamNum[next]!=(teamNum[now]+1)%2 :  
                    # 집합 번호가 있는데 이전 노드와 집합 번호가 같다면 break
                    isBN=False
                    break
            if not isBN : break
    if not isBN : break
```

