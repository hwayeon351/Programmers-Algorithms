from collections import deque
from copy import deepcopy
from itertools import permutations

def bfs(sr, sc, er, ec, board):
    dr = [-1, 0, 1, 0]
    dc = [0, -1, 0, 1]
    visit = [[0] * 4 for _ in range(4)]
    visit[sr][sc] = 1
    q = deque([[sr, sc, 0]])

    while q:
        r, c, cnt = q.popleft()
        if r == er and c == ec:
            return cnt

        for ddr, ddc in zip(dr, dc):
            nr = r
            nc = c
            move = []
            for i in range(1, 4):
                nr += ddr
                nc += ddc
                if nr < 0 or nr >= 4 or nc < 0 or nc >= 4:
                    nr -= ddr
                    nc -= ddc
                    move.append([nr, nc])
                    break

                if board[nr][nc] > 0:
                    move.append([nr, nc])
                    break

            if len(move) > 0:
                if visit[move[0][0]][move[0][1]] or (move[0][0] == r and move[0][1] == c): continue
                visit[move[0][0]][move[0][1]] = 1
                q.append([move[0][0], move[0][1], cnt+1])
            else:
                if visit[nr][nc]: continue
                visit[nr][nc] = 1
                q.append([nr, nc, cnt + 1])

        for ddr, ddc in zip(dr, dc):
            nr = r + ddr
            nc = c + ddc
            if 0 <= nr < 4 and 0 <= nc < 4:
                if visit[nr][nc]: continue
                visit[nr][nc] = 1
                q.append([nr, nc, cnt + 1])

def solution(board, r, c):
    answer = -1
    card = [[] for _ in range(7)]
    kinds = 0
    for y in range(4):
        for x in range(4):
            if board[y][x] > 0:
                card[board[y][x]].append([y, x])
                if kinds < board[y][x]: kinds = board[y][x]

    idx = [i for i in range(1, kinds+1)]
    per = list(permutations(idx, kinds))

    for p in per:
        nr = r
        nc = c
        cnt = 0
        copy_board = deepcopy(board)
        for i in range(len(p)):
            choice0 = bfs(nr, nc, card[p[i]][0][0], card[p[i]][0][1], copy_board)
            choice1 = bfs(nr, nc, card[p[i]][1][0], card[p[i]][1][1], copy_board)
            if choice0 < choice1:
                cnt += choice0
                cnt += 1
                nr = card[p[i]][0][0]
                nc = card[p[i]][0][1]
                cnt += bfs(nr, nc, card[p[i]][1][0], card[p[i]][1][1], copy_board)
                cnt += 1
                nr = card[p[i]][1][0]
                nc = card[p[i]][1][1]
            else:
                cnt += choice1
                cnt += 1
                nr = card[p[i]][1][0]
                nc = card[p[i]][1][1]
                cnt += bfs(nr, nc, card[p[i]][0][0], card[p[i]][0][1], copy_board)
                cnt += 1
                nr = card[p[i]][0][0]
                nc = card[p[i]][0][1]
            copy_board[card[p[i]][0][0]][card[p[i]][0][1]] = 0
            copy_board[card[p[i]][1][0]][card[p[i]][1][1]] = 0

        if answer == -1 or answer > cnt:
            answer = cnt
            
    return answer
