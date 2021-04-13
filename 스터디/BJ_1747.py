n = int(input())

def is_pel(number):
    l, r = 0, len(number)-1
    while l < r:
        if number[l]==number[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

def is_prime(number):
    num = int(number**(0.5))
    for i in range(2, num+1):
        if number%i == 0:
            return False
    return True

if n==1:
    n = 2
    
while True:
    if is_pel(str(n)) and is_prime(n):
        print(n)
        break
    n += 1