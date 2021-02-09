import sys

input = sys.stdin.readline

case = int(input())
ans=[]
for c in range(case):
    n, m = map(int, input().split())
    que = list(map(int, input().split()))

    num = que[m]
    count = 1
    start_index = 0  # 다음 중요도의 문서의 시작 인덱스
    last_index = 0  # 해당 중요도 문서의 마지막 인덱스

    # 해당 문서보다 중요도가 높은 문서의 개수 count
    for i in range(9,num,-1):  # 중요도 9부터 시작
        for j in range(start_index, len(que)):
            if que[j]==i:
                count+=1
                last_index=j

        for j in range(0, start_index):
            if que[j]==i:
                count+=1
                last_index=j  
        start_index=last_index

    # 궁금한 문서와 중요도가 같은 문서들

    if start_index<=m:  # 인덱스 m이  시작 인덱스보다 클 경우
        for j in range(start_index, m):
            if que[j]==num:
                count+=1
    else :  # 인덱스 m이 시작인덱스보다 작을 경우
        for j in range(start_index, len(que)):
            if que[j]==num:
                count+=1
        for j in range(0, m):
            if que[j]==num:
                count+=1

    ans.append(count)
print('\n'.join(map(str,ans)))