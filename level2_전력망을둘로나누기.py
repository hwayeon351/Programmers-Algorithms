from collections import deque, defaultdict


def bfs(start_v, graph, visit):
    q = deque([start_v])
    visit[start_v] = 1
    total = 1
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if not visit[nv]:
                q.append(nv)
                visit[nv] = 1
                total += 1
    return total


def solution(n, wires):
    answer = n
    d_wires = deque(wires)
    for _ in range(len(wires)):
        broken_wire = d_wires.popleft()
        visit = [0] * (n + 1)
        tops = []
        graph = defaultdict(list)
        for v1, v2 in d_wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        for v in range(1, n + 1):
            if not visit[v]:
                tops.append(bfs(v, graph, visit))
        answer = min(abs(tops[0] - tops[1]), answer)
        d_wires.append(broken_wire)
    return answer
