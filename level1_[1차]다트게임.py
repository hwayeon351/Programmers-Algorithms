def cal_score(s, b, op, score):
    s **= b
    if op == "*":
        if len(score) > 0:
            score[-1] *= 2
        score.append(s*2)
    elif op == "#":
        score.append(-s)
    else: score.append(s)
    
def solution(dartResult):
    score = []
    option = ['*','#']
    s = 0
    b = 0
    op = ""
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            if i != 0:
                cal_score(s, b, op, score)
                s = 0
                b = 0
                op = ""
            if dartResult[i] == '1':
                if dartResult[i+1] == '0':
                    s = 10
                    i += 1
                else: s = 1
            else: s = int(dartResult[i])
        elif dartResult[i] == 'S':
            b = 1
        elif dartResult[i] == 'D':
            b = 2
        elif dartResult[i] == 'T':
            b = 3
        elif dartResult[i] in option:
            op = dartResult[i]
        if i == len(dartResult)-1:
            cal_score(s, b, op, score)
        i += 1
    return sum(score)
