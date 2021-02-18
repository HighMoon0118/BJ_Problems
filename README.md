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



### 15683번 문제 : 감시

> 삼성 기출 문제답게 구현문제이다. 항상 문제를 풀고나서 다른 사람들은 어떻게 풀었는지 보곤 하는데 나보다 10배나 빠르게 푼 사람이 있어서 글을 남긴다.
>
> 나는 모든 경우에서 cctv가 바라보는 곳을 전부 그래프에 체크해주고 마지막에 사각지대의 개수를 세서 답을 도출했는데 이러한 과정에서 계속 그래프를 deepcopy해줘야하는 낭비가 생겼다.
>
> 하지만, 이 분은 set을 사용하여 cctv가 바라보는 좌표를 넣으며 문제를 풀었다. 이렇게 풀면 새로운 그래프를 계속 만들지 않아도 될 뿐만 아니라 답을 도출할 때 그래프를 다 탐색하지 않아도 set의 길이만큼 빼주면 된다. 
>
> 또한 나는 바라보는 방향마다 케이스를 나눠서 코드가 길어졌는데, 이 분은 각 방향마다 변하는 row, column값을 리스트에 넣어 for문을 돌렸다.  생각하기 귀찮아서 막 코드를 짰는데 앞으론 좀 더 신경을 써야곘다.

```python
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)

def look_at(r, c, direction):
    check = set()
    for i in range(4):
        new_r, new_c = r + dr[i], c + dc[i]
        while 0 <= new_r < N and 0 <= new_c < M:
            if board[new_r][new_c] == 6: break
            if board[new_r][new_c] == 0: check.add((new_r, new_c))
            new_r, new_c = new_r + dr[d], new_c + dc[d]

    return check
```



### 15684번 문제 : 사다리 조작

> 파이썬으로 풀면 계속 시간초과가 나왔다...  
>
> 하루 종일 이 문제랑 씨름하느라 스트레스를 너무 많이 받았는데 언어만 자바로 바꿔서 풀었더니 바로 통과했다. 물론 파이썬으로 푼 사람도 몇명 보였다. 내 실력 부족이겠지..ㅠㅠ
>
> 다른 사람의 풀이에선 각 사다리 열마다 가로줄의 개수를 센 다음, 가로줄의 개수가 홀수인 사다리 열의 개수가 현재 내가 놓을 수 있는 가로줄보다 많으면 탐색을 멈췄다. 즉, 내가 현재 놓을 수 있는 가로줄로 모든열의 가로줄 개수를 짝수로 만들 수 없다면 불가능하다고 판단하는 것이다.
>
> 내가 이 문제를 처음 접했을 때, 모든 열의 가로줄이 짝수인지 아닌지로 풀었다가 두개의 열에 3개, 3개의 가로줄이 있어도 답이 된다는 반례가 있다는 것을 알고 포기했었는데 좀 더 고민했더라면 풀었을라나..



### 5430번 문제 : AC

>a = [1,2,3,4] 라는 리스트가 있고 L=1, R=2 라고 하자.
>
>리스트 a를 인덱스 L부터 R까지 얕은복사를 하는 방법은 a[L:R+1]이다. 그러면 인덱스 R부터 L까지 얕은복사를 하는 방법은 a[R:L-1:-1]일까? 아니다.
>
>만약 L이 0이라면 a[R:L-1:-1]은 a[2 :-1 :-1 ]가 될 것이고 이는 []이다. 왜그럴까? 이는 슬라이싱에서 -1은 마지막 인덱스를 나타내기 때문이다.
>
>앞으로 문제를 풀 때, 이를 주의하면서 풀어야겠다.



### 1713번 문제 : 후보 추천하기

> 나는 처음에 사진틀에 후보가 중복되면 안되기 때문에 set을 사용했고, 리스트 안에 [추천수, 인덱스, 후보번호]를 넣고 각 요소를 기준으로 정렬하며 문제를 풀었다.
>
> 사진틀의 수나 추천 횟수가 커진다면 정렬때문에 분명 시간초과가 나는 풀이다.
>
> 이 문제에서 사진을 삭제하는 우선순위는 추천수 > 게시시간 이고 학생번호가 최대 100인것을 이용하면 효율적으로 문제를 풀 수 있다.
>
> 학생별로 추천을 받은 수를 저장할 크기 101의 배열을 만들고,  추천 순서대로 학생을 저장할 크기 n인 리스트를 만들어주면 된다. **for문을 돌면서 자연스럽게 게시시간 순대로 도는 것이 이 풀이의 핵심이다.**

```python
n = int(input())
vote = int(input())
votes = list(map(int, input().split()))
vote_count = [0 for _ in range(101)]
board = []

for v in votes:
    if vote_count[v]:
        vote_count[v] += 1
    else:
        board.append(v)
        vote_count[v] = 1

    if len(board) > n:
        min_vote = 1001
        for i in range(len(board) - 1):
            if vote_count[board[i]] < min_vote:
                min_vote = vote_count[board[i]]
                who = board[i]
        board.remove(who)
        vote_count[who] = 0
board.sort()
print(*board)
```



### 15658번 문제 : 연산자 끼워넣기(2)

> 파이썬에서 어떤 음수를 나눈 몫을 구할 땐 연산자 //를 사용하는 것이 아닌
>
> 연산자 /로 나눠주고 int로 형변환을 시켜줘야 한다.

```python
a = -5
a//=2  # a = -3
b = -5
b/=2  # b = -2.5
b=int(b)  # b = -2
```

