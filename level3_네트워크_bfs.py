def dfs(now_com, visit, computers):
    visit[now_com] = True
    for i in range(0, len(computers)):
        if i!=now_com and computers[now_com][i] == 1:
            if visit[i] == False:
                dfs(i, visit, computers)

def solution(n, computers):
    answer = 0
    visit = [False]*n
    for i in range(0, n):
        if visit[i] == False:
            dfs(i, visit, computers)
            answer+=1
    return answer
