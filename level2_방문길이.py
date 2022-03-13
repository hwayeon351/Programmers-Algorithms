def solution(dirs):
    answer = 0
    direction = {'U': 3, 'D': 1, 'R': 2, 'L': 0}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visit = [[[0]*11 for _ in range(11)] for _ in range(4)]
    x, y = 5, 5
    
    for dir in dirs:
        now_d = direction[dir]
        nx = x + dx[now_d]
        ny = y + dy[now_d]

        if nx < 0 or nx > 10 or ny < 0 or ny > 10: continue
        if visit[now_d][y][x] or visit[(now_d+2)%4][ny][nx]: 
            x = nx
            y = ny
            continue
            
        visit[now_d][y][x] = 1
        visit[(now_d+2)%4][ny][nx] = 1
        x = nx
        y = ny
        answer += 1
    
    return answer
