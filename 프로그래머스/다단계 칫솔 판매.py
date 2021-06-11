def solution(enroll, referral, seller, amount):
    
    parentOf = {enroll[i]:referral[i] for i in range(len(enroll))}
        
    asset = {person:0 for person in enroll}
    amount = [money*100 for money in amount]
    
    for i in range(len(seller)):
        who = seller[i]
        money = amount[i]
        asset[who] += money
        
        while who in parentOf and money//10:
            money = money//10
            asset[who] -= money
            if parentOf[who] == "-": break
            who = parentOf[who]
            asset[who] += money
    
    answer = [asset[who] for who in enroll]
    return answer