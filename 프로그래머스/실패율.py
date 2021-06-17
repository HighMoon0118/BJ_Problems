def solution(N, stages):
    ans = [[i, 0] for i in range(N+1)]
    
    cnt = [0]*(N+2)
    
    for i in stages:
        cnt[i] += 1
        
    users = cnt[N+1]
    for i in range(N, 0, -1):
        success = users
        users += cnt[i]
        total = users
        if total:
            ans[i][1] = (total-success)/total
            
    ans = sorted(ans[1:], key=lambda x: (-x[1], x[0]))
    ans = [i for i, a in ans]
    
    return ans