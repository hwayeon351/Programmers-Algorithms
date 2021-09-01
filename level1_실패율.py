from collections import Counter
def solution(N, stages):
    answer = []
    stage_user = Counter(stages)
    before_user = 0
    for s in range(1, N+1):
        if s not in stage_user:
            answer.append([s, 0])
        else:
            answer.append([s, stage_user[s]/(len(stages)-before_user)])
            before_user += stage_user[s]
    answer.sort(key=lambda x:(-x[1], x[0]))
    return [i[0] for i in answer]
