import sys

input = sys.stdin.readline

n = input().strip()
count = [0 for _ in range(10)]
for num in n:
    if num=='6' or num=='9':
        count[ord('6')-ord('0')]+=1
    else :
        count[ord(num)-ord('0')]+=1
count[6]=count[6]//2 if count[6]%2==0 else count[6]//2+1
print(max(count))