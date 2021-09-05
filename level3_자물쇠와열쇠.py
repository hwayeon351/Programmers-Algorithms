import copy
def lotate_key(key):
    keys = []
    keys.append(key)
    #1.
    new_key = []
    for i in range(0, len(key)):
        row = []
        for j in range(len(key)-1, -1, -1):
            row.append(key[j][i])
        new_key.append(row)
    keys.append(new_key)
    
    #2.
    new_key = []
    for i in range(len(key)-1, -1, -1):
        row = []
        for j in range(len(key)-1, -1, -1):
            row.append(key[i][j])
        new_key.append(row)
    keys.append(new_key)
    
    #3.
    new_key = []
    for i in range(len(key)-1, -1, -1):
        row = []
        for j in range(len(key)):
            row.append(key[j][i])
        new_key.append(row)
    keys.append(new_key)
    return keys
    
        
def solution(key, lock):
    keys = lotate_key(key)
    for k in keys:
        for dr in range(-(len(lock)), len(lock)+1):
            for dc in range(-(len(lock)), len(lock)+1):
                visit = copy.deepcopy(lock)
                for r in range(len(key)):
                    for c in range(len(key)):
                        nr = r+dr
                        nc = c+dc
                        if 0 <= nr < len(lock) and 0 <= nc < len(lock):
                            #열쇠 돌기 - 자물쇠 돌기 또는 열쇠 홈 - 자물회 홈인 경우,
                            if lock[nr][nc] == k[r][c]: break
                            #열쇠 돌기 - 자물쇠 홈인 경우
                            if lock[nr][nc] == 0 and k[r][c] == 1:
                                visit[nr][nc] = 1
                    else: continue
                    break
                else:
                    for v in visit:
                        if 0 in v: break
                    else: return True
    return False
