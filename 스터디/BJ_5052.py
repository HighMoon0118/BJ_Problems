import sys

input = sys.stdin.readline

t = int(input())
ans = []
zero = ord('0')

def isConsist():

    trie = {}

    for i in range(n):
        mTrie = trie
        for j in range(len(num[i])):
            idx = int(num[i][j])

            if idx not in mTrie:
                mTrie[idx] = {}
            elif j==len(num[i])-1:
                return False
            mTrie = mTrie[idx]
    return True

for _ in range(t):

    n = int(input())
    num = [input().strip() for _ in range(n)]

    num.sort(key = lambda x: -len(x))

    if isConsist(): ans.append("YES")
    else: ans.append("NO")


print("\n".join(ans))