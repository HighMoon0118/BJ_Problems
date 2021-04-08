import sys

input = sys.stdin.readline
def pel(w):
    global delete

    l, r = 0, len(w)-1
    while l<r:
        if w[l]!=w[r]:
            if delete: return False
            delete = 1
            if pel(w[l:r]) or pel(w[l+1:r+1]):
                return True
            return False
        else:
            l += 1
            r -= 1
    return True


n = int(input())
ans = []
for _ in range(n):

    word = input().strip()
    delete = 0
    is_pel = pel(word)

    if not is_pel: ans.append("2")
    elif delete: ans.append("1")
    else: ans.append("0")
print("\n".join(ans))