from collections import deque
answer = -1

def bfs(maps):
    global answer
    visit = [[0]*len(maps[0]) for _ in range(len(maps))]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque()
    q.append([0, 0, 1])
    visit[0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == len(maps[0])-1 and y == len(maps)-1:
            answer = cnt
            return
        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                if not maps[ny][nx]: continue
                if visit[ny][nx]: continue
                visit[ny][nx] = 1
                q.append([nx, ny, cnt+1])
                
    
def solution(maps):
    bfs(maps)
    return answer
