def find(node, parent):
    if parent[node] == node:
        return node
    return find(parent[node], parent)
    
def make_set(node, parent, rank):
    parent[node] = node
    rank[node] = 0

def union(n1, n2, parent, rank):
    root1 = find(n1, parent)
    root2 = find(n2, parent)    
    if rank[root1] == rank[root2]:
        parent[root1] = root2
        rank[root2]+=1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else: parent[root2] = root1
    
def solution(n, costs):
    mst = []
    parent = dict()
    rank = dict()
    answer = 0
    for nd in range(n):
        make_set(nd, parent, rank)
    costs.sort(key = lambda x:x[2])
    for c in costs:
        n1, n2, cost = c
        if find(n1, parent) != find(n2, parent):
            union(n1, n2, parent, rank)
            answer += cost
            mst.append([n1, n2])
            if len(mst) == n-1: return answer
    return answer
