import sys

input = sys.stdin.readline

def makeIt(parent, left, right):
    global idx 
    for i in range(left, right):
        if preorder[parent] == inorder[i]:
            makeIt(parent+1, left, i)
            makeIt(parent+1+i-left, i+1, right)
            postorder[idx] = preorder[parent]
            idx += 1
            return


case = int(input())

ans = []

for _ in range(case):
    n = int(input())

    preorder = list(map(int, input().split()))
    inorder =list(map(int, input().split()))
    postorder = [0]*n
    idx = 0
    makeIt(0, 0, n)
    ans.append(" ".join(map(str, postorder)))

print("\n".join(ans))