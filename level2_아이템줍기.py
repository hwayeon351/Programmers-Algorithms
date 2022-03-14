from collections import deque

def bfs(board, itemX, itemY, cx, cy, rectangle):
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    q = deque([[cx, cy, 0]])
    visit = [[0] * 201 for _ in range(201)]
    visit[cy][cx] = 1

    while q:
        x, y, cnt = q.popleft()

        if x == itemX and y == itemY:
            return cnt

        for ddx, ddy in zip(dx, dy):
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx <= 200 and 0 <= ny <= 200 and not visit[ny][nx] and board[ny][nx]:
                for sx, ey, ex, sy in rectangle:
                    if nx in range(sx, ex+1) and ny in range(sy, ey+1):
                        if nx in range(sx + 1, ex) and ny in range(sy + 1, ey):
                            break

                else:
                    visit[ny][nx] = 1
                    q.append([nx, ny, cnt + 1])


def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0] * 201 for _ in range(201)]
    itemX *= 2
    itemY = (100 - itemY) * 2
    characterX *= 2
    characterY = (100 - characterY) * 2

    for i in range(len(rectangle)):
        rectangle[i][1] = 100 - rectangle[i][1]
        rectangle[i][3] = 100 - rectangle[i][3]
        for j in range(4):
            rectangle[i][j] *= 2
        for y in range(rectangle[i][3], rectangle[i][1] + 1):
            for x in range(rectangle[i][0], rectangle[i][2] + 1):
                board[y][x] = 1

    return bfs(board, itemX, itemY, characterX, characterY, rectangle)//2
