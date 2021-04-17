global answer
global visit

def dfs(idx, cnt, target, words):
    global answer
    global visit
    if words[idx] == target:
        if answer == -1: answer = cnt
        elif cnt < answer: answer = cnt
        return
    for i in range(len(words[idx])):
        for j in range(len(words)):
            if j!=idx and words[j][:i] == words[idx][:i] and words[j][i+1:] == words[idx][i+1:]:
                if visit[j] == False:
                    visit[j] = True
                    dfs(j, cnt+1, target, words)
                    visit[j] = False                    
        
def solution(begin, target, words):
    global answer
    global visit
    answer = -1
    for i in range(len(begin)):
        for j in range(len(words)):
            if words[j][:i] == begin[:i] and words[j][i+1:] == begin[i+1:]:
                visit = [False]*len(words)
                visit[j] = True
                dfs(j, 1, target, words)
    if answer == -1: return 0
    else: return answer
