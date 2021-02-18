import sys

input = sys.stdin.readline

def makeAnswer(i):
    global min_s, max_s
    if i==n-1:
        number = num[0]
        for j in range(n-1):
            if how[j]==0:
                number += num[j+1]
            elif how[j]==1:
                number -= num[j+1]
            elif how[j]==2:
                number *= num[j+1]
            else:
                number /= num[j+1]
                number = int(number)
        min_s = min(min_s, number)
        max_s = max(max_s, number)
        return


    for j in range(4):
        if way[j]:
            way[j]-=1
            how[i]=j
            makeAnswer(i+1)
            way[j]+=1

n = int(input())
num = list(map(int, input().split()))
way = list(map(int, input().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈
how = [0 for _ in range(n-1)]
min_s = 1000000000
max_s = -1000000000
makeAnswer(0)
print(max_s)
print(min_s)