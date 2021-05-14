import sys

def preorder(p):
    result = p
    if tree[p][0] != '.':
        result += preorder(tree[p][0])
    if tree[p][1] != '.':
        result += preorder(tree[p][1])
    return result

def inorder(p) :
    result = ''
    if tree[p][0] != '.':
        result += inorder(tree[p][0])
    result += p
    if tree[p][1] != '.':
        result += inorder(tree[p][1])
    return result

def postorder(p) :
    result = ''
    if tree[p][0] != '.':
        result += postorder(tree[p][0])
    if tree[p][1] != '.':
        result += postorder(tree[p][1])
    result += p
    return result

input = sys.stdin.readline

n = int(input())
tree = dict()
for _ in range(n):
    p, c1, c2 = input().split()
    tree[p] = [c1, c2]

print(preorder('A'))
print(inorder('A'))
print(postorder('A'))