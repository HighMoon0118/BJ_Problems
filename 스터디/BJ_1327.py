import sys
from collections import deque

input = sys.stdin.readline

def is_asc(word):
    for i in range(n-1):
        if word[i]>word[i+1]:
            return False
    return True

def make_it():
    que = deque()
    que.append((num, 0))

    while que:
        word, cnt = que.popleft()

        if is_asc(word): 
            return cnt

        if word in words: 
            continue
        words.add(word)

        for i in range(n-k+1):
            que.append((word[:i]+word[i+k-1:i-1-n:-1]+word[i+k:], cnt+1))
    return -1


n, k = map(int, input().split())
num = "".join(input().split())
words = set()
print(make_it())