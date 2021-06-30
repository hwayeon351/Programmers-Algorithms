from collections import deque
def bfs(i, visit, n, computers):
    queue = deque([i])
    while queue:
        front = queue.popleft()
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
