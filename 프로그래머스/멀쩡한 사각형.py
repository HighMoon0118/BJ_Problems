def solution(w,h):
    total = w*h
    h, w = max(w, h), min(w, h)
    num = gcd(h, w)
    w//=num
    h//=num
    if w == 1: cnt = h*w*num
    else: cnt = ((h//w)+1)*w*num
    return total - cnt

def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)

print(solution(7,4))