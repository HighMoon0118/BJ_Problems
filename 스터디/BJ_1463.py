from collections import deque

n = int(input())
visited = [0 for _ in range(n+1)]

def bfs():
    que = deque()

    que.append(n)
    cnt = 0

    while que:
        tmp = deque()

        while que:
            num = que.popleft()

            if num == 1: return cnt

            if visited[num]: continue
            visited[num] = 1

            if num%3 == 0:
                tmp.append(num//3)
            if num%2 == 0:
                tmp.append(num//2)
            tmp.append(num-1)
            
        que = tmp
        cnt += 1

print(bfs())