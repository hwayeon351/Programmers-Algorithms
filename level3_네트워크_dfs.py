def dfs(i, visit, n, computers):
    for idx in range(n):
        if i!=idx and computers[i][idx] and visit[idx]==False:
            visit[idx] = True
            dfs(idx, visit, n, computers)
            
def solution(n, computers):
    answer = 0
    visit = [False]*len(computers)
    for i in range(len(computers)):
        if visit[i]==False:
            visit[i] = True
            dfs(i, visit, n, computers)
            answer+=1
    return answer
