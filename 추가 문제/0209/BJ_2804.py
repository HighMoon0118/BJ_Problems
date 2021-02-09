a, b = input().split()

r, c = -1, -1

for i, charA in enumerate(a):
    for j, charB in enumerate(b):
        if charA==charB:
            r, c = j, i
            break
    if r!=-1:
        break

a_idx, b_idx = 0, 0
ans = ""
for i in range(len(b)):
    if i==r:
        ans+=a
        b_idx+=1
    else:
        for j in range(len(a)):
            if j==c:
                ans+=b[b_idx]
                b_idx+=1
            else:
                ans+="."
    ans+="\n"
print(ans)