import sys, heapq

input = sys.stdin.readline
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
tc = 0
ans = []
while True:
    tc += 1
    n = int(input())
    if n==0: break

    board = [[0]*(n+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(n)]+[[0]*(n+2)]
    dist = [[0]*(n+2)]+[[0]+[2500 for _ in range(n)]+[0] for _ in range(n)]+[[0]*(n+2)]
    dist[1][1] = board[1][1]
    heap = [(board[1][1], (1,1))]
    while heap:
        d, now = heapq.heappop(heap)
        if now == (n, n): break
        for i in range(4):
            nr, nc = now[0]+dr[i], now[1]+dc[i]
            if dist[nr][nc] > d + board[nr][nc]:
                dist[nr][nc] = d + board[nr][nc]
                heapq.heappush(heap, (dist[nr][nc], (nr, nc)))
    ans.append("Problem {}: {}".format(tc, dist[n][n]))
print("\n".join(ans))