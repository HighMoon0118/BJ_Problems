import sys

input = sys.stdin.readline

n = int(input())

order = list(map(int, input().split()))

line = []  # 줄
num = n

for o in order[::-1]:  # 가장 키가 큰 사람부터 시작, 본인보다 큰 사람이 있는 만큼 오른쪽으로 이동해서 삽입
    line.insert(o, num)
    num-=1

print(*line)