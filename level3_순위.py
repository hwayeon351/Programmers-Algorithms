from collections import defaultdict
def solution(n, results):
    answer = 0
    #key = 사람, value = key를 이긴 사람
    winner = defaultdict(set)
    #key = 사람, value = key한테 진 사람
    loser = defaultdict(set)
    for win, lose in results:
        winner[lose].add(win)
        loser[win].add(lose)
    for i in range(1, n+1):
        #i를 이긴 사람들은 i한테 진 사람들도 이긴다
        for w in winner[i]:
            loser[w].update(loser[i])
        #i한테 진 사람들은 i를 이긴 사람들한테도 진다
        for l in loser[i]:
            winner[l].update(winner[i])
    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n-1: answer += 1
    return answer
