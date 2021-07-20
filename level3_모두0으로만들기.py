import sys
from collections import defaultdict
sys.setrecursionlimit(300000)
def dfs(now_i, before_i, visit, adj, a):
    global answer
    for next_i in adj[now_i]:
        if not visit[next_i]:
            visit[next_i] = True
            dfs(next_i, now_i, visit, adj, a)
    a[before_i] += a[now_i]
    answer += abs(a[now_i])
    a[now_i] = 0
      
def solution(a, edges):
    global answer
    answer = 0
    if sum(a)!=0: return -1
    if a.count(0) == len(a): return 0
    adj = defaultdict(set)
    for n1, n2 in edges:
        adj[n1].add(n2)
        adj[n2].add(n1)
    visit = [False]*len(a)
    dfs(0, 0, visit, adj, a)
    return answer
