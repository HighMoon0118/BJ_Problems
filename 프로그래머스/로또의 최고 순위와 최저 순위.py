def solution(lottos, win_nums):

    lottos.sort(reversed=True)
    cnt = 0
    zero = 0
    for num in lottos:
        if num==0: 
            zero += 1
            break
        if num in win_nums:
            cnt +=1

    answer = [cnt, cnt+zero]
    return answer