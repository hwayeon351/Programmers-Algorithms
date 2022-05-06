from collections import defaultdict
def dfs(node, sheep, wolf, visit, can_go):
    global answer, infos, tree
    visit[node] = 1
    can_go += tree[node]
    
    if infos[node]: wolf += 1
    else: sheep += 1
    
    if wolf >= sheep: return
    if sheep > answer: answer = sheep
    
    for n in can_go:
        go = [nn for nn in can_go if nn != n and not visit[nn]]
        dfs(n, sheep, wolf, visit[:], go)
    
    
def solution(info, edges):
    global answer, infos, tree
    infos = info
    answer = 0
    tree = defaultdict(list)
    for p, c in edges:
        tree[p].append(c)
        
    visit = [0]*len(info)
    dfs(0, 0, 0, visit, [])
    
    return answer
