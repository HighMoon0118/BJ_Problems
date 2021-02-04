import sys

input = sys.stdin.readline

def check_left(num) :
    left = start[num]+6
    a = left%8 if left>=8 else left
    return gear[num][a]

def check_right(num) :
    right = start[num]+2
    a = right%8 if right>=8 else right
    return gear[num][a]  

gear = []
start = [0 for _ in range(4)]
for i in range(4) :
    gear.append(input())

n = int(input())
for _ in range(n) :
    num, how = map(int, input().split())

    status = [0 for _ in range(3)]  # 서로 같은 극인지 아닌지
    rotate = [0 for _ in range(4)]  # 시계로 회전하는지 반시계로 회전하는지
    rotate[num-1] = how

    for i in range(3) :  # 현재 톱니 상태 저장
        if check_right(i)==check_left(i+1) :
            status[i]=1
        else : status[i]=-1

    left = right = num-1
    l_how = r_how = how
    while left>0 :  # 기준 톱니 왼쪽 체크
        left-=1
        if status[left]==-1 :
            rotate[left]=-1*l_how
            l_how = rotate[left]
        elif status[left]==1 :
            l_how = 0
    while right<3 : # 기준 톱니 오른쪽 체크
        right+=1
        if status[right-1]==-1 :
            rotate[right]=-1*r_how
            r_how = rotate[right]
        elif status[right-1]==1 :
            r_how = 0

    for i in range(4) :  # 회전한 톱니바퀴에서 12시에 위치한 index 저장
        if rotate[i]==1 :
            start[i]+=7
        elif rotate[i]==-1 :
            start[i]+=1
        start[i]%=8
ans = 0
for i in range(4) :
    if gear[i][start[i]]=='1' :
        ans+=2**i  
print(ans)

