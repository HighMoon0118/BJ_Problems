import sys

input = sys.stdin.readline

def trans_from():
    result = 0
    for i, num in enumerate(nums[::-1]):
        result += num*(a**i)
    return result

def trans_to(num):
    result = []
    while num//b:
        result.append(num%b)
        num//=b
    result.append(num)
    return result[::-1]


a, b = map(int, input().split())
m = int(input())
nums = list(map(int,input().split()))

ans = trans_to(trans_from())
print(*ans)