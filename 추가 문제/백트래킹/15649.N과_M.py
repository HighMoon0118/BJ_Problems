n, m = map(int, input().split())

def makeAnswer(s, c):
    if c==m:
        ans.append(" ".join(map(str, num)))
        return
    for i in range(1, n+1):
        if not used[i]:
            used[i] = 1
            num[c] = i
            makeAnswer(i+1, c+1)
            used[i] = 0

ans = []
used = [0 for _ in range(n+1)]
num = [0 for _ in range(m)]

makeAnswer(1,0)
print("\n".join(ans))