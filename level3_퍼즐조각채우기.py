from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def get_rotated_blocks(blocks):
    i = len(blocks)
    while i > 0:
        i -= 1
        b_len, block = blocks[i]
        blocks[i].append(i)
        ori_block = block
        for _ in range(3):
            new_block = []
            for y in range(len(ori_block[0])):
                row = []
                for x in range(len(ori_block)-1, -1, -1):
                    row.append(ori_block[x][y])
                new_block.append(row)
            blocks.append([b_len, new_block, i])
            ori_block = blocks[-1][1]

    blocks.sort(key=lambda x:x[2])



def fill_puzzle(puzzles, blocks):
    answer = 0
    visit = [0]*(blocks[-1][-1]+1)
    blocks = deque(blocks)
    for p_len, puzzle in puzzles:
        i = len(blocks)
        while i > 0:
            i -= 1
            b_len, block, id = blocks.popleft()
            if visit[id]: continue

            if p_len != b_len or len(puzzle) != len(block) or len(puzzle[0]) != len(block[0]):
                blocks.append([b_len, block, id])
                continue
            check = True
            for y in range(len(puzzle)):
                for x in range(len(puzzle[0])):
                    if puzzle[y][x] == block[y][x]:
                        check = False
                        break
            if check:
                visit[id] = 1
                answer += p_len
                break
            blocks.append([b_len, block, id])
    return answer


def get_blocks(block_range, table):
    blocks = []
    for length, sx, ex, sy, ey in block_range:
        new_block = []
        for y in range(sy, ey+1):
            row = []
            for x in range(sx, ex+1):
                row.append(table[y][x])
            new_block.append(row)
        blocks.append([length, new_block])

    return blocks

def get_block_range(table, n):
    visit = [[0] * len(table[0]) for _ in range(len(table))]
    blocks = []
    for y in range(len(table)):
        for x in range(len(table[0])):
            if table[y][x] == n and not visit[y][x]:
                q = deque([[x, y]])
                sx, ex = x, x
                sy, ey = y, y
                visit[y][x] = 1
                length = 1
                while q:
                    now_x, now_y = q.popleft()
                    for ddx, ddy in zip(dx, dy):
                        nx = now_x + ddx
                        ny = now_y + ddy
                        if 0 <= nx < len(table[0]) and 0 <= ny < len(table):
                            if table[ny][nx] == n and not visit[ny][nx]:
                                visit[ny][nx] = 1
                                q.append([nx, ny])
                                if ex < nx: ex = nx
                                if ey < ny: ey = ny
                                if sx > nx: sx = nx
                                if sy > ny: sy = ny
                                length += 1
                blocks.append([length, sx, ex, sy, ey])
    return blocks


def solution(game_board, table):

    blocks_range = get_block_range(table, 1)
    blocks = get_blocks(blocks_range, table)
    get_rotated_blocks(blocks)
    
    puzzles_range = get_block_range(game_board, 0)
    puzzles = get_blocks(puzzles_range, game_board)


    return fill_puzzle(puzzles, blocks)
