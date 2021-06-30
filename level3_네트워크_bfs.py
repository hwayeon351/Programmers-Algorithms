def bfs(i, visit, n, computers):
    queue = [i]
    while queue:
        front = queue.pop()
        visit[front] = True
        for idx in range(n):
            if front!=idx and computers[front][idx] and visit[idx]==False:
                queue.append(idx)
            
def solution(n, computers):
    answer = 0
    visit = [False]*len(computers)
    for i in range(len(computers)):
        if visit[i]==False:
            bfs(i, visit, n, computers)
            answer+=1
    return answer
