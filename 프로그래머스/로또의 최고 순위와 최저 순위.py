def solution(lottos, win_nums):

    cnt = 0
    zero = 0
    for i in range(6):
        if lottos[i]==0:
            zero += 1
            continue
        if lottos[i] in win_nums:
            cnt += 1
    MAX = zero + cnt
    if MAX==0: MAX=1
    MIN = 1 if cnt==0 else cnt

    answer = [7-MAX, 7-MIN]
    return answer