from collections import defaultdict
def dfs(t_from, visit, t_dict, num):
    global answer
    visit += t_from
    if len(visit)//3 == num:
        if answer=="": 
            answer = visit
        else: answer=min(visit, answer)
        return
    
    if len(t_dict[t_from]) == 0:
        return
    
    for i, t_to in enumerate(t_dict[t_from]):
        if t_to[1]==False:
            t_dict[t_from][i][1] = True
            dfs(t_to[0], visit, t_dict, num)
            t_dict[t_from][i][1] = False
            
def solution(tickets):
    global answer
    answer = ""
    t_dict = defaultdict(list)
    for k, v in tickets:
        t_dict[k].append([v,False])
        t_dict[k].sort()
    dfs("ICN", "", t_dict, len(tickets)+1)
    return list(map(''.join, zip(*[iter(answer)]*3)))
