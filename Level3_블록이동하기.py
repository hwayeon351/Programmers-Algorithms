#8, 12, 14 테케 통과 못함
from collections import defaultdict, deque

rotate = [[1, 0, 1, 1], [-1, 0, -1, 1], [1, 0, 1, -1], [-1, 0, -1, -1], [0, 1, 1, 1], [0, 1, -1, 1], [0, -1, 1, -1],
          [0, -1, -1, -1]]
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def play(board, N):
    visit = defaultdict(int)
    visit['0010'] = 1
    q = deque([[[[0, 0], [1, 0]], 0]])

    while q:
        r, sec = q.popleft()
        if (r[0][0] == N and r[0][1] == N) or (r[1][0] == N and r[1][1] == N): return sec

        # 회전
        if r[0][0] - r[1][0] == 0:
            for d in range(4):
                check_x = r[0][0] + rotate[d][0]
                check_y = r[0][1] + rotate[d][1]
                nx = r[0][0] + rotate[d][2]
                ny = r[0][1] + rotate[d][3]
                if not (0 <= check_x <= N and 0 <= check_y <= N and 0 <= nx <= N and 0 <= ny <= N): continue
                if board[check_y][check_x] or board[ny][nx]: continue
                if (abs(nx-r[1][0]) + abs(ny-r[1][1])) != 1: continue
                v = str(nx) + str(ny) + str(r[1][0]) + str(r[1][1])
                if visit[v] > 0: continue
                q.append([[[nx, ny], [r[1][0], r[1][1]]], sec + 1])
                visit[v] = 1

            for d in range(4):
                check_x = r[1][0] + rotate[d][0]
                check_y = r[1][1] + rotate[d][1]
                nx = r[1][0] + rotate[d][2]
                ny = r[1][1] + rotate[d][3]
                if not (0 <= check_x <= N and 0 <= check_y <= N and 0 <= nx <= N and 0 <= ny <= N): continue
                if board[check_y][check_x] or board[ny][nx]: continue
                if (abs(nx-r[0][0]) + abs(ny-r[0][1])) != 1: continue
                v = str(r[0][0]) + str(r[0][1]) + str(nx) + str(ny)
                if visit[v] > 0: continue
                q.append([[[r[0][0], r[0][1]], [nx, ny]], sec + 1])
                visit[v] = 1

        else:
            for d in range(4, 8):
                check_x = r[0][0] + rotate[d][0]
                check_y = r[0][1] + rotate[d][1]
                nx = r[0][0] + rotate[d][2]
                ny = r[0][1] + rotate[d][3]
                if not (0 <= check_x <= N and 0 <= check_y <= N and 0 <= nx <= N and 0 <= ny <= N): continue
                if board[check_y][check_x] or board[ny][nx]: continue
                if (abs(nx - r[1][0]) + abs(ny - r[1][1])) != 1: continue
                v = str(nx) + str(ny) + str(r[1][0]) + str(r[1][1])
                if visit[v] > 0: continue
                q.append([[[nx, ny], [r[1][0], r[1][1]]], sec + 1])
                visit[v] = 1

            for d in range(4, 8):
                check_x = r[1][0] + rotate[d][0]
                check_y = r[1][1] + rotate[d][1]
                nx = r[1][0] + rotate[d][2]
                ny = r[1][1] + rotate[d][3]
                if not (0 <= check_x <= N and 0 <= check_y <= N and 0 <= nx <= N and 0 <= ny <= N): continue
                if board[check_y][check_x] or board[ny][nx]: continue
                if (abs(nx - r[0][0]) + abs(ny - r[0][1])) != 1: continue
                v = str(r[0][0]) + str(r[0][1]) + str(nx) + str(ny)
                if visit[v] > 0: continue
                q.append([[[r[0][0], r[0][1]], [nx, ny]], sec + 1])
                visit[v] = 1

        # 이동
        for m in range(4):
            rx1 = r[0][0] + move[m][0]
            ry1 = r[0][1] + move[m][1]
            rx2 = r[1][0] + move[m][0]
            ry2 = r[1][1] + move[m][1]
            if not (0 <= rx1 <= N and 0 <= ry1 <= N and 0 <= rx2 <= N and 0 <= ry2 <= N): continue
            if board[ry1][rx1] or board[ry2][rx2]: continue
            v = str(rx1) + str(ry1) + str(rx2) + str(ry2)
            if visit[v] > 0: continue
            visit[v] = 1
            q.append([[[rx1, ry1], [rx2, ry2]], sec + 1])


def solution(board):
    return play(board, len(board) - 1)
