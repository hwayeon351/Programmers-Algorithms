from collections import defaultdict
def solution(n, results):
    answer = 0
    win_d = defaultdict(set)
    lose_d = defaultdict(set)
    for winner, loser in results:
        win_d[winner].add(loser)
        lose_d[loser].add(winner)
    for i in range(1, n+1):
        #i를 이긴 사람은 i한테 진 사람도 이긴다.
        for winner in lose_d[i]:
            win_d[winner].update(win_d[i])
        #i한테 진 사람은 i를 이긴 사람한테도 진다.
        for loser in win_d[i]:
            lose_d[loser].update(lose_d[i])
    for i in range(1, n+1):
        if len(win_d[i])+len(lose_d[i]) == n-1:
            answer += 1
    return answer
