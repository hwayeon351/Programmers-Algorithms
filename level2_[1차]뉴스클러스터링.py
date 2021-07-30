from collections import Counter
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    A = []
    B = []
    i = 0
    #다중 집합 만들기
    while i <= max(len(str1)-2, len(str2)-2):
        if i <= len(str1)-2:
            if str1[i].isalpha() and str1[i+1].isalpha(): A.append(str1[i] + str1[i+1])
        if i <= len(str2)-2:
            if str2[i].isalpha() and str2[i+1].isalpha(): B.append(str2[i] + str2[i+1])
        i+=1
        
    #A와 B가 공집합인 경우
    if len(A) == len(B) == 0: return 65536
    
    #유사도 계산
    counterA = Counter(A)
    counterB = Counter(B)
    inter_AB = 0
    for k in counterA.keys():
        inter_AB += min(counterA[k], counterB[k])
    sum_AB = sum(counterA.values()) + sum(counterB.values()) - inter_AB
    return int(inter_AB/sum_AB*65536)
