import sys

input = sys.stdin.readline

def makeIt(next):
    global finish, ans
    if finish: return
    if next==m:
        finish = True
        ans = 1
        return
    
    a, b = clause[next][0], clause[next][1]

    if not used[a] and not used[b]:  # 두 변수 모두 사용한적 없을 때
        # aa는 a의 절대값의 boolean값
        for aa in boolean:
                for bb in boolean:
                    if a*aa>0 or b*bb>0:
                        if (a==b and aa!=bb) or (a+b==0 and aa!=bb):  # 두 변수가 같을 때
                            continue
                        used[a] = aa if a>0 else -aa
                        used[-a] = -used[a]
                        used[b] = bb if b>0 else -bb
                        used[-b] = -used[b]
                        makeIt(next+1)
                        used[a] = used[-a] = used[b] = used[-b] = 0
    elif not used[a]:  # 변수 a만 사용한적 없을 때
        for aa in boolean:
            if a*aa>0 or used[b]>0:
                used[a] = aa if a>0 else -aa
                used[-a] = -used[a]
                makeIt(next+1)
                used[a] = used[-a] = 0
    elif not used[b]:  # 변수 b만 사용한적 없을 때
        for bb in boolean:
            if b*bb>0 or used[a]>0:
                used[b] = bb if b>0 else -bb
                used[-b] = -used[b]
                makeIt(next+1)
                used[b] = used[-b] = 0
    elif used[a]==-1 and used[b]==-1:  # 두 변수 모두 사용했을 때 둘다 False면
        return
    else:
        makeIt(next+1)

n, m = map(int, input().split())
clause = [list(map(int, input().split())) for _ in range(m)]
used = [0 for _ in range(2*n+1)]
boolean = [-1, 1]
ans, finish = 0, False
makeIt(0)
print(ans)