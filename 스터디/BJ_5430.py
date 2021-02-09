import sys

input = sys.stdin.readline

c = int(input())
ans = []

for _ in range(c):
    how = input().strip()
    n = int(input())
    line = input().strip()

    result=""
    d_num = how.count("D")
    if d_num > n:  # D의 개수가 숫자보다 많으면 error
        result = "error"
    elif d_num == n:  # D의 개수가 숫자와 같다면 []
        result="[]"
    else:
        l, r, flip = 0, n, False
        numbers = list(map(int, line[1:-1].split(",")))
        for c in how:
            if c == "R":  # R일 땐 문자열 뒤집기
                flip = True if not flip else False
            elif flip:  # 뒤집어져 있다면 r-1
                r-=1
            else:  # 뒤집어져 있지 않다면 l+1
                l+=1
        tmp = numbers[l:r]  # 인덱스 l부터 R까지 복사
        if flip: 
            result = "["+",".join(map(str,tmp[::-1]))+"]"  # 뒤집어져 있다면 반대로 출력
        else: 
            result = "["+",".join(map(str,tmp))+"]"  # 아니라면 정상 출력

    ans.append(result)
print("\n".join(ans))