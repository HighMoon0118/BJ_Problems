import sys

input = sys.stdin.readline

word = input().strip()
words = set()

for i in range(len(word)):
    for j in range(i+1, len(word)+1):
        words.add(word[i:j])
print(len(words))