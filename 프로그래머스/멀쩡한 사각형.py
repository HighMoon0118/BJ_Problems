def solution(w,h):
    total = w*h
    cnt = w+h
    h, w = max(w, h), min(w, h)
    num = gcd(h, w)
    w//=num
    h//=num
    cnt -= num
    return total - cnt

def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)