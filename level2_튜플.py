def solution(s):
    answer = []
    s = s[2:-2]
    ss = s.split('},{')
    ss.sort(key = len)
    for ns in ss:
        ns = ns.split(',')
        for n in ns:
            if n not in answer: answer.append(n)
    return list(map(int, answer))
