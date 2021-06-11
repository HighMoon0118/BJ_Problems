
t = int(input())

def makeIt(number, ):

    if dp[number]: return dp[number]

    for i in range(number+1):
        possible = True
        for s in str(i):
            if not num[int(s)]:
                possible = False
                break
        if possible

    

for tc in range(1, t+1):
    n, o, m = map(int, input().split())
    num = [0]*10
    for i in map(int, input()):
        num[i] = 1
    how = [0]*4
    for i in map(int, input().split()):
        how[i] = 1
    w = int(input())

    dp = [0]*1000
