import sys

input = sys.stdin.readline

n = int(input())

order = list(map(int, input().split()))

line = []  # 줄
num = n

for o in order[::-1]:
    line.insert(o, num)
    num-=1

print(*line)