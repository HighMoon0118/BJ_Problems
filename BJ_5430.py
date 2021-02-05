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
    if d_num > n:
        result = "error"
    elif d_num == n:
        result="[]"
    else:
        l, r, flip = 0, n, False
        numbers = list(map(int, line[1:-1].split(",")))
        for c in how:
            if c == "R":
                flip = True if not flip else False
            elif flip:
                r-=1
            else:
                l+=1
        tmp = numbers[l:r]
        if flip: 
            result = "["+",".join(map(str,tmp[::-1]))+"]"
        else: 
            result = "["+",".join(map(str,tmp))+"]"

    ans.append(result)
print("\n".join(ans))