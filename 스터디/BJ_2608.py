def make_num(word):
    result = 0
    for c in to_num.keys():
        while word.startswith(c):
            result += to_num[c]
            word = word[len(c):]
    return result

def make_word(num):
    result = ""
    for n in to_st.keys():
        while num >= n:
            result += to_st[n]
            num -= n
    return result

to_num = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
to_st = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}

a = input().strip()
b = input().strip()

sum = make_num(a) + make_num(b)
print(sum)
print(make_word(sum))