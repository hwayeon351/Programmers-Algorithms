from collections import deque
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(board):
    MAX = len(board)*len(board)*600
    q = deque()
    visit = [[[MAX]*len(board) for _ in range(len(board))] for _ in range(4)]
    if board[0][1] == 0:
        visit[0][0][1] = 100
        q.append([1,0,0,100])
    if board[1][0] == 0:
        visit[1][1][0] = 100
        q.append([0,1,1,100])
    for i in range(4):
        visit[i][0][0] = 100
    while q:
        now_x, now_y, now_d, cost = q.popleft()
        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board):
                if board[ny][nx]: continue
                if i == now_d:
                    new_cost = cost + 100
                else:
                    new_cost = cost + 600
                if visit[i][ny][nx] > new_cost:
                    visit[i][ny][nx] = new_cost
                    q.append([nx, ny, i, new_cost])
    min_cost = MAX
    for i in range(4):
        if min_cost > visit[i][-1][-1]: min_cost = visit[i][-1][-1]
    return min_cost
    
def solution(board):
    return bfs(board)
