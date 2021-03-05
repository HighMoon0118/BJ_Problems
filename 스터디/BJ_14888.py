import sys

input = sys.stdin.readline

def makeIt(c):
    global maxN, minN
    if c == len(cal):
        result = num[0]
        for i in range(n-1):
            if cal[i] == 0:
                result += num[i+1]
            elif cal[i] == 1:
                result -= num[i+1]
            elif cal[i] == 2:
                result *= num[i+1]
            elif cal[i] == 3:
                result /= num[i+1]
                result = int(result)
        if result > maxN:
            maxN = result
        if result < minN:
            minN = result
        return 

    for i in range(4):
        if how[i]:
            how[i] -= 1
            cal[c] = i
            makeIt(c+1)
            how[i] += 1


n = int(input())
num = list(map(int, input().split()))
how = list(map(int, input().split())) # +, -, *, //
cal = [0 for _ in range(n-1)]
maxN, minN = -1000000000, 1000000000
makeIt(0)
print(maxN)
print(minN)