def dfs(i, target, words, visit, cnt):
    global answer
    if words[i] == target:
        if answer == 0 or answer > cnt: answer = cnt
        return
    if cnt == len(visit)-1: return
    for b_i in range(len(words[i])):
        for idx, w in enumerate(words):
            if words[i][:b_i]==w[:b_i] and words[i][b_i+1:]==w[b_i+1:] and visit[idx]==False:
                visit[idx] = True
                dfs(idx, target, words, visit, cnt+1)
                visit[idx] = False

def solution(begin, target, words):
    global answer
    if target not in words: return 0
    answer = 0
    words.append(begin)
    visit = [False]*len(words)
    visit[-1] = True
    dfs(-1, target, words, visit, 0)
    
    return answer
