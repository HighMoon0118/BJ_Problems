def makeIt(i, way, bit):

    if dp[i][way][bit]>=0: return dp[i][way][bit]
    result = 0
    for j, w in link[i][way]:
        if bit & (1<<j) == 0:
            result = max(result, makeIt(j, w, bit|(1<<j)))

    dp[i][way][bit] = boxes[i][way] + result
    return dp[i][way][bit]

t = int(input())
ans = []
for tc in range(1, t+1):
    n = int(input())

    boxes = [list(map(int,input().split(" "))) for _ in range(n)]

    box_3 = [[(min(box[1], box[2]), max(box[1], box[2])), 
    (min(box[0], box[2]), max(box[0], box[2])), 
    (min(box[0], box[1]), max(box[0], box[1]))] for box in boxes]

    link = [[[] for _ in range(3)] for _ in range(n)]

    for i in range(n):
        for j in range(i+1, n):
            for a in range(3):
                for b in range(3):
                    if box_3[i][a][0]>=box_3[j][b][0] and box_3[i][a][1]>=box_3[j][b][1]:
                        link[i][a].append((j, b))
                    if box_3[j][a][0]>=box_3[i][b][0] and box_3[j][a][1]>=box_3[i][b][1]:
                        link[j][a].append((i, b))

    dp = [[[-1]*(1<<n) for _ in range(3)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(3):
            result = max(result, makeIt(i, j, 1<<i))
    ans.append(f"#{tc} {result}")
print("\n".join(ans))