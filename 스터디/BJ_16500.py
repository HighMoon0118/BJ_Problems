def make_it(word):
    global possible
    if not word:
        possible = 1
        return
    index = len(s)-len(word)
    if dp[index]:
        return
    dp[index] = 1
    for i in range(n):
        if word.startswith(a[i]):
            make_it(word[len(a[i]):])

s = input().strip()
n = int(input())
a = []
for _ in range(n):
    a.append(input().strip())
dp = [0 for _ in range(len(s))]
possible = 0
make_it(s)
print(possible)