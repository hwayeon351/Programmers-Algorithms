def find_erase_block(brd):
    erase = []
    for i in range(len(brd)-1):
        for j in range(len(brd[0])-1):
            c = brd[i][j]
            if c == '0': continue
            if brd[i][j+1] == c and brd[i+1][j+1] == c and brd[i+1][j] == c:
                erase.append((i,j))
                erase.append((i,j+1))
                erase.append((i+1,j))
                erase.append((i+1,j+1))
    return list(set(erase))

def solution(m, n, board):
    answer = 0
    brd = []
    erase = []
    for i in range(len(board)):
        brd.append(list(board[i]))
    erase = find_erase_block(brd)
    while(len(erase) > 0):
        answer += len(erase)
        for i, j in erase:
            brd[i][j] = "0"
        for i in range(m-1, -1, -1):
            for j in range(n):
                if brd[i][j] == "0":
                    for k in range(i-1, -1, -1):
                        if(brd[k][j] != "0"):
                            brd[i][j] = brd[k][j]
                            brd[k][j] = "0"
                            break
        erase = find_erase_block(brd)
    return answer
