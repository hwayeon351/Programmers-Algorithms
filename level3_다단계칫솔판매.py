def solution(enroll, referral, seller, amount):
    levels = dict()
    earns = dict()
    for e, r in zip(enroll, referral):
        levels[e] = r
        earns[e] = 0
    for s, a in zip(seller, amount):
        e = a*100
        refer = levels[s]
        while refer != '-':
            fee = e//10
            earns[s] += (e-fee)
            e = fee
            s = refer
            refer = levels[s]
            if e == 0: break
        else: earns[s] += (e-e//10)
    return list(earns.values())
