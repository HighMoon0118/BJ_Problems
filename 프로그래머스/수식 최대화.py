oper = ["+", "-", "*"]
how = [0,0,0]
used = [0,0,0]

NUMS = []
OPERS = []
ans = 0

def makeIt(cnt):
    global ans
    
    if cnt == 3:
        nums = NUMS[:]
        opers = OPERS[:]
        
        for i in how:
            o = oper[i]
            
            j = 0
            while j < len(opers):
                if opers[j] == o:
                    if o == "+":
                        nums[j] += nums[j+1]
                    elif o == "-":
                        nums[j] -= nums[j+1]
                    elif o == "*":
                        nums[j] *= nums[j+1]
                    nums.pop(j+1)
                    opers.pop(j)
                else:
                    j += 1
        ans = max(ans, abs(nums[0]))
        return
    
    for i in [0, 1, 2]:
        if not used[i]:
            how[cnt] = i
            used[i] = 1
            makeIt(cnt+1)
            used[i] = 0

def solution(expression):
    i = j = 0
    
    while i<len(expression):
        s = expression[i]
        
        if s in ["+", "-", "*"]:
            NUMS.append(int(expression[j:i]))
            OPERS.append(s)
            j = i+1
        i += 1
    NUMS.append(int(expression[j:i]))
    
    makeIt(0)
    return ans