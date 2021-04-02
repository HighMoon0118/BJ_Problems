import sys

input = sys.stdin.readline


# class Trie:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False

#     def add(self, word):
#         trie = self
#         for c in word:
#             if not trie.children.get(c):
#                 trie.children[c] = Trie()
#             trie = trie.children[c]
#         trie.is_end = True

#     def search(self, word):
#         trie = self
#         for c in word:
#             if not trie.children.get(c):
#                 return False
#             trie = trie.children[c]
#         if not trie.is_end:
#             return False
#         return True

# n, m = map(int, input().split())

# trie = Trie()

# for _ in range(n):
#     trie.add(input().strip())
# ans = 0
# for i in range(m):
#     if trie.search(input().strip()):
#         ans += 1

# print(ans)

n, m = map(int, input().split())
words = set()
for _ in range(n):
    words.add(input().strip())
ans = 0
for _ in range(m):
    if input().strip() in words:
        ans += 1
print(ans)