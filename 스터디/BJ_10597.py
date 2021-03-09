import sys

input = sys.stdin.readline

def makeIt(index, c):
    global finish, ans
    if finish: return

    if index==len(num):
        if c==maxN:
            finish = True
            ans = " ".join(map(str, tmp))
        return
    # 한자리 숫자나 두자리 숫자로 탐색
    num1 = int(num[index])
    if not used[num1]:  # 만약 한자리 숫자가 사용되지 않았다면 재귀 ㄱㄱ
        used[num1] = True
        tmp[c] = num1
        makeIt(index+1, c+1)
        used[num1] = False
    if index<len(num)-1:  # 만약 두자리 숫자가 사용되지 않았다면 재귀 ㄱㄱ
        num2 = int(num[index:index+2])
        if num2 < maxN+1 and not used[num2]:
            used[num2] = True
            tmp[c] = num2
            makeIt(index+2, c+1)
            used[num2] = False
            
num = input().strip()
if len(num)<10:
    maxN = len(num)
else:
    maxN = 9+(len(num)-9)//2
used = [0 for _ in range(maxN+1)]
tmp = [0 for _ in range(maxN)]
finish = False
makeIt(0,0)
print(ans)