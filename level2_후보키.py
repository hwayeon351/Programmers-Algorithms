from itertools import combinations
def solution(relation):
    answer = 0
    candidate = [[] for _ in range(len(relation[0])+1)]
    attr = [i for i in range(len(relation[0]))]
    for r in range(1, len(attr)+1):
        #1. n C r = 예비 후보키 조합 생성
        combi = combinations(attr, r)
        #2. 각 예비 후보키가 후보키가 될 수 있는지 체크
        for c in combi:
            #2-1. 유일성 체크
            visit = []
            for t in relation:
                data = ""
                for key in c:
                    data += t[key]
                #유일성을 만족하지 않는다
                if data in visit: break
                visit.append(data)
                
            #유일성을 만족한 경우
            #2-2. 최소성 체크
            else:
                new_candi = list(c)
                for i in range(1, len(new_candi)+1):
                    ck = True
                    #현재 후보키
                    for candi in candidate[i]:
                        for a in candi:
                            if a in new_candi: continue
                            else: break
                        #현재 후보키의 모든 속성이 예비 후보키에 있는 경우
                        else:
                            ck = False
                            break
                    if not ck: break
                else:
                    candidate[len(new_candi)].append(new_candi)
    
    for c in candidate:
        answer += len(c)
    return answer
