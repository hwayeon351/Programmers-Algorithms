def bfs(i, visit, computers):
    queue = []
    queue.append(i)
    while(len(queue) > 0):
        com = queue.pop(0)
        visit[com] = True
        for i in range(0, len(computers)):
            if i != com and visit[i] == False and computers[com][i]:
                queue.append(i)

def solution(n, computers):
    answer = 0
    visit = [False]*n
    for i in range(0, n):
        if visit[i] == False:
            bfs(i, visit, computers)
            answer+=1
    return answer
