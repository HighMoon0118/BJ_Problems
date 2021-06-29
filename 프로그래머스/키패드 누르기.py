def dist(num1, num2):
    num1 -= 1
    num2 -= 1
    
    r1, c1 = num1//3, num1%3
    r2, c2 = num2//3, num2%3
    
    return abs(r1-r2) + abs(c1-c2)

def solution(numbers, hand):
    
    left, right = 10, 12
    ans = ""
    for num in numbers:
        if num == 0: num = 11
        
        if num == 1 or num == 4 or num == 7:
            ans += "L"
            left = num
        elif num == 3 or num == 6 or num == 9:
            ans += "R"
            right = num
        else:
            d1, d2 = dist(left, num), dist(right, num)
            if d1 < d2:
                ans += "L"
                left = num
            elif d1 > d2:
                ans += "R"
                right = num
            elif hand == "right":
                ans += "R"
                right = num
            else:
                ans += "L"
                left = num
    return ans