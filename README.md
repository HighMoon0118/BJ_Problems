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



### 2479번 문제 : 경로 찾기

> 이 문제는 직접 인접 행렬을 만들어야 하는 문제이다.
>
> 또한 경로를 역 추적하기 위해서 순서를 넣을 리스트도 따로 만들어야한다.
>
> 오랜만에 풀어보는 유형이라 고생좀 했다...

```python
def makeBoard():  # 인접행렬 만드는 함수, 한 비트만 다를경우 연결
    for i in range(1, n+1):
        for j in range(1, n+1):
            diff = num[i]^num[j]
            count = 0
            for b in range(k):
                if diff&(1<<b):
                    count+=1
            if count==1:
                board[i][j]=1
                board[j][i]=1
```

```python
    ans = [b]
    i = b
    while i!=a:  # order리스트 안에 순서를 넣고 역 추적
        d -= 1
        for j in range(1, n+1):
            if check[i][j] and order[j]==d:
                ans.append(j)
                i = j
                break
```



### 1325번 문제 : 효율적인 해킹

> 처음엔 dfs나 bfs을 사용하여 b -> a로 이동하면서 자식 수를 셌는데 시간초과가 났다.
>
> 두번째 방법으론 a -> b로 이동하면서 해당 b번 노드와 연결된 노드개수를 세주면서 풀었다. 
>
> 물론 이 방법으로도 시간초과가 났지만 한 노드의 자식 개수를 셀 때, 모든 노드에서 해당 노드의 부모노드로 이동하면서 부모노드의 자식수를 하나씩 증가시켜주면서 자식 개수를 셀 수 있다는 것을 알았다.
>
> 실버2 문제임에도 불구하고 사이클이 있는 그래프여서 일반적인 dfs나 bfs로는 파이썬 코드가 통과되지 않았다. 물론 파이썬으로 푼 사람이 있었지만 입출력의 시간을 줄였거나 정말 복잡한 알고리즘을 사용하지 않았나 싶다. 
>
> 나중에 좀 더 실력이 늘면 다시 풀어봐야겠다.



### 11277번 문제 : 2-SAT - 1

>나는 이 문제를 풀 때 음수 인덱스를 사용해서 좀더 간단하게 풀었다고 생각했는데
>
>다른 사람의 코드를 보면서 아 이런방법도 있었지... 깨닫게 돼서 다신 까먹지 않도록 기록으로 남기기로 했다.

``` python
a, b = clause[i]
graph[-a].add(b)
graph[-b].add(a)
```

> 이런식으로 그래프를 만들어 주어 dfs로 빠르게 풀 수 있었다.
>
> a or b 가 True라고 가정할 때, a가 False이면 b가 True이여만 하고, b가 False이면 a가 True이여만 한다. 
>
> graph[a].add(b)와 graph[a].add(-b)를 함께 쓰지 않는 이유는 b가 True아니면 False이여야 하는데 둘 다 일수는 없기 때문이다.
>
> graph[a].add(-b); graph[b].add(-a) 를 해도 답을 도출할 수 있다.



### 1865번 문제 : 웜홀

> 벨만포드 알고리즘은 최단거리 문제에서 음수 사이클이 있는경우 사용하는 알고리즘이다. 시작지점이 있는 경우엔
>
> ```python
> if time[s] != MAX_TIME and time[e] > time[s]+t:
>     	time[e] = time[s]+t
> ```
>
> 이런식으로 시작지점에서 S까지 연결돼있는지 확인을 하고 최단거리를 업데이트 해줘야 한다. 그래야 시작지점으로부터 갈 수 있는 지점과 없는 지점을 구별할 수 있기 때문이다.
>
> 하지만, 이 문제는 단지 그래프에 음수 사이클이 있는지 여부를 따지는 문제이기 때문에
>
> ```python
> if time[e] > time[s]+t:
>     	time[e] = time[s]+t
> ```
>
> 이렇게 E까지 걸리는 시간을 업데이트 해주고, N번째에도 업데이트가 생긴다면 사이클이 있는 것으로 판단하면 된다. 만약에 연결 여부를 확인하게 되면 시작지점으로부터 갈 수 없는 곳에 음수 사이클이 존재 할 수 있기 때문에 제대로 판별 할 수 없기 때문이다.



### 1219번 문제 : 오민식의 고민

> 이 문제는 음수 사이클이 존재할 수 있는 벨만포드 문제이다. 이전에 다른 벨만포드 문제를 다익스트라로 푸는 사람이 있어 나도 한번 다익스트라로 풀어보려고 했다. 
>
> 처음 접근은 도착지점에 오기 전에 사이클을 만나는지 안만나는지를 구분했는데 도착했어도 돈을 더 벌어서 도착지점에 올 수 있다면 이동을 해도 되는 문제였다. 그래서 도착 전과 후에 사이클이 있는지 체크하면서 문제를 풀었지만 사이클이 있다고 해도 사이클을 돌고 도착지점에 도착하지 못하면 돈을 무한정 벌 수 없다는 것을 깨닫고 다르게 접근했다.
>
> 바로 음수 사이클을 돈 객체와 아닌 객체로 나눠서 문제를 푸는 것이다. 그런데 분명 알고리즘에 이상이 없다고 생각했지만 자꾸 틀린 답이 나왔다. 한시간 정도 고민하다 뭐가 틀렸는지 찾았는데 처음 다익스트라로 문제를 접근 했을 때, 왔던 지점을 또 오게되면 사이클이라고 판단했던 것이었다. 다른 사람이 다익스트라로 풀었다고 그냥 다익스트라로 풀면 되겠다고 생각을 해서인지 처음부터 잘못 풀고 있었던 것이다. 
>
> 다익스트라는 이전에 왔던 노드를 재 방문할 수 없지만 이 문제는 음수가 존재하는 그래프이기에 한 노드에 재 방문할 수가 있어 내 풀이가 계속 틀렸던 것이다. 이 문제를 해결하기 위해서 객체마다 지나온 경로를 저장하여 사이클을 찾아냈고 해결할 수 있었다.



### 1327번 문제 : 소트 게임

> 처음 이 문제를 풀 때, 어떻게 뒤집어야 가장 빨리 오름차순으로 만들까 고민했었지만
>
> n이 8보다 작다는 것을 깨닫고 완탐을 하면 되겠구나 생각했다.
>
> 하지만, 최소 개수를 구하는 문제임에도 DFS로 풀었고 시간초과가 나오게 되었다.
>
> 최단거리 문제는 BFS로 풀어야 한다는 것을 잊지말자.

```python
def make_it():
    que = deque()
    que.append((num, 0))

    while que:
        word, cnt = que.popleft()

        if is_asc(word): 
            return cnt

        if word in words: 
            continue
        words.add(word)

        for i in range(n-k+1):
            que.append((word[:i]+word[i+k-1:i-1-n:-1]+word[i+k:], cnt+1))
    return -1
```



### SWEA 5204번 문제 : 병합 정렬

> n이 최대 1000000이 주어지는 문제이다. 병합정렬을 해주기 위해선 잠시 배열을 옮겨두는 temp를 만들어야 하는데 나는 테스트케이스마다 temp를 새로 만들다보니 런타임 오류가 계속 나게 되었다...
>
> 이 문제때문에 얼마나 시간을 날린건지..ㅠㅠ

```python
def merge(l, r):
    global cnt
    if r-l==1: return

    mid = (l+r)>>1
    merge(l, mid)
    merge(mid, r)

    i, s, e = l, l, mid
    if num[mid-1] > num[r-1]: cnt += 1
    while i < r:
        if r == e or s < mid and num[s] <= num[e]:
            temp[i] = num[s]
            s += 1
        else:
            temp[i] = num[e]
            e += 1
        i += 1
    i = l
    while i < r:
        num[i] = temp[i]
        i += 1

t = int(input())
ans = []
temp = [0]*1000000  # 효율적인 코딩

for tc in range(1, t+1):
    n = int(input())
    num = list(map(int, input().split()))
    # temp = [0 for _ in range(n)] 이런식으로 코딩했었는데 메모리낭비, 시간낭비였다.
    cnt = 0
    merge(0, n)
    ans.append(f"#{tc} {num[n//2]} {cnt}")
print("\n".join(ans))
```



### 백준 11052번 문제 : 카드 구매하기

> 카드 구매하기 문제는 DP문제이다. DP문제는 어떻게 설계하느냐에 따라 시간이 오래 걸릴 수도 적게 걸릴 수도 있기 때문에 설계가 가장 중요한 이슈이다.
>
> 이 문제를 풀긴 했지만 다른 사람들보다 20배정도 느리게 나와서 왜 그럴까 고민하게 되었다. 설계를 할 당시 



### 백준 1600번 문제 : 말이 되고픈 원숭이

> 이문제는 dp로 풀면 풀리지 않는 문제이다. 정확히는 dp[][][][][][][][][x] [y] [k] 로 풀면 풀리지 않는다.

```
4
6 10
0 0 1 1 1 1
0 1 1 0 1 1
0 1 1 1 1 0
0 1 1 1 1 0
0 1 1 1 1 0
0 1 1 1 1 0
0 1 1 0 1 1
0 1 1 1 1 1
1 1 1 1 0 0
1 0 0 1 1 0
```

> 위 반례를 보면 알 수 있다. (6, 3)에 k번 말처럼 이동해서 올 수 있는 방법은 두가지가 있다. 하지만 해당 지점에 도착하기 위해 움직인 횟수가 다르기 때문에 위처럼 DP를 만들면 풀 수 없다.
>
> BFS로 풀긴 했지만 DP로 풀려면 어떻게 해야할까?
>
> dp [x] [y] [k]를 사용하되, 어떤 지점에 몇번만에 도착했는지 기록해놓는 2차 배열을 만들어서 만약 해당 지점의 dp에 값이 있더라도 더 적은 횟수로 도착했다면 dp를 다시 만드는 식으로 풀면 된다.