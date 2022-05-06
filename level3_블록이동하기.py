from collections import deque

def bfs(R, C):
    global brd, rotate
    # (r1, c1), (r2, c2), d
    # d = 0 -> 가로, d = 1 -> 세로
    visit = [[[[[0] * len(brd[0]) for _ in range(len(brd))] for _ in range(len(brd[0]))] for _ in
               range(len(brd))] for _ in range(2)]
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    robot = [[0, 0], [0, 1], 0]
    visit[robot[2]][robot[0][0]][robot[0][1]][robot[1][0]][robot[1][1]] = 1
    q = deque([[robot, 0]])

    while q:
        rb, sec = q.popleft()
        if (rb[0][0] == R and rb[0][1] == C) or (rb[1][0] == R and rb[1][1] == C):
            return sec

        #90도 회전
        for l in range(2):
            for i in range(2):
                r = rb[(l+1)%2][0]
                c = rb[(l+1)%2][1]
                nr1 = rb[l][0] + rotate[rb[2]][l][i][0][0]
                nc1 = rb[l][1] + rotate[rb[2]][l][i][0][1]
                nr2 = rb[l][0] + rotate[rb[2]][l][i][1][0]
                nc2 = rb[l][1] + rotate[rb[2]][l][i][1][1]
                if not (0 <= nr1 <= R and 0 <= nr2 <= R and 0 <= nc1 <= C and 0 <= nc2 <= C): continue
                if brd[nr1][nc1] or brd[nr2][nc2]: continue
                if rb[2] == 0:
                    if r < nr2:
                        r1, c1, r2, c2 = r, c, nr2, nc2
                    else:
                        r1, c1, r2, c2 = nr2, nc2, r, c
                    if visit[1][r1][c1][r2][c2]: continue
                    visit[1][r1][c1][r2][c2] = 1
                    q.append([[[r1, c1], [r2, c2], 1], sec+1])

                else:
                    if c < nc2:
                        r1, c1, r2, c2 = r, c, nr2, nc2
                    else:
                        r1, c1, r2, c2 = nr2, nc2, r, c
                    if visit[0][r1][c1][r2][c2]: continue
                    visit[0][r1][c1][r2][c2] = 1
                    q.append([[[r1, c1], [r2, c2], 0], sec+1])

        #한 칸 이동
        for ddr, ddc in zip(dr, dc):
            r1 = rb[0][0] + ddr
            c1 = rb[0][1] + ddc
            r2 = rb[1][0] + ddr
            c2 = rb[1][1] + ddc
            if not (0 <= r1 <= R and 0 <= r2 <= R and 0 <= c1 <= C and 0 <= c2 <= C): continue
            if brd[r1][c1] or brd[r2][c2]: continue
            if visit[rb[2]][r1][c1][r2][c2]: continue
            visit[rb[2]][r1][c1][r2][c2] = 1
            q.append([[[r1, c1], [r2, c2], rb[2]], sec+1])

def solution(board):
    global brd, rotate
    brd = board
    rotate = [
        #d = 0일 때,
        [[[[1, 0], [1, 1]], [[-1, 0], [-1, 1]]], [[[1, 0], [1, -1]], [[-1, 0], [-1, -1]]]],
        #d = 1일 때,
        [[[[0, 1], [1, 1]], [[0, -1], [1, -1]]], [[[0, 1], [-1, 1]], [[0, -1], [-1, -1]]]]
    ]

    return  bfs(len(board)-1, len(board[0])-1)
