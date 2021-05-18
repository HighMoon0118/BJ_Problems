import sys

input = sys.stdin.readline

n = int(input())
inOrder = tuple(map(int, input().split()))
postOrder = tuple(map(int, input().split()))

print(inOrder, postOrder)