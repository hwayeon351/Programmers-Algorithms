from itertools import permutations
def solution(k, dungeons):
    answer = 0
    per = permutations([i for i in range(len(dungeons))])
    
    for p in per:
        tired = k
        cnt = 0
        for i in p:
            if dungeons[i][0] > tired: continue
            tired -= dungeons[i][1]
            cnt += 1
        if answer < cnt: answer = cnt
    
    return answer
