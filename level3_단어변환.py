def dfs(i, target, words, visit, cnt):
    global answer
    if words[i] == target:
        if answer > cnt: answer = cnt
        return
    if cnt == len(visit): return
    for b_i in range(len(words[i])):
        for idx, w in enumerate(words):
            if words[i][:b_i]==w[:b_i] and words[i][b_i+1:]==w[b_i+1:] and visit[idx]==False:
                visit[idx] = True
                dfs(idx, target, words, visit, cnt+1)
                visit[idx] = False

def solution(begin, target, words):
    global answer
    if target not in words: return 0
    answer = len(words)
    visit = [False]*len(words)
    for b_i in range(len(begin)):
        for i, w in enumerate(words):
            if w[:b_i]==begin[:b_i] and w[b_i+1:]==begin[b_i+1:]:
                visit[i] = True 
                dfs(i, target, words, visit, 1)
                visit[i] = False
    return answer
