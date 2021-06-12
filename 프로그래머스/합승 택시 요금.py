def solution(n, s, a, b, fares):
    MAX = 20000001
    tree = [[20000001]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        tree[i][i] = 0
    
    for aa, bb, c in fares:
        tree[aa][bb] = c
        tree[bb][aa] = c
        
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                tree[i][j] = min(tree[i][j], tree[i][k] + tree[k][j])
                tree[j][i] = tree[i][j]
    answer = MAX
    for i in range(1, n+1):
        answer = min(answer, tree[s][i]+tree[i][a]+tree[i][b])
    return answer