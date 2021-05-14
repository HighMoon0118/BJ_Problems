# import sys
# sys.setrecursionlimit(100000)
# input = sys.stdin.readline

# def postorder(start, end):
#     global idx
#     if start==end:
#         ans[idx] = num[start]
#         idx += 1
#         return
#     elif start > end:
#         return
    
#     parent = num[start]
#     child = start+1
#     while num[child] < parent:
#         child += 1
#         if child == len(num):
#             break
#     postorder(start+1, child-1)
#     postorder(child, end)
#     ans[idx] = parent
#     idx += 1

# num = []
# idx = 0
# while True:
#     try: num.append(int(input()))
#     except: break
# ans = [0]*len(num)
# postorder(0, len(num)-1)
# print('\n'.join(map(str, ans)))


import sys
from bisect import bisect
sys.setrecursionlimit(100000)
input = sys.stdin.readlines


def postorder(s, e):
    if s == e: return
    d = preorder[s]
    idx = bisect(preorder, d, s, e)
    postorder(s + 1, idx)
    postorder(idx, e)
    print(d)


preorder = list(map(int, input()))
postorder(0, len(preorder))