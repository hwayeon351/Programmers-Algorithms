def solution(n, s):
    if n > s: return [-1]
    elif n == 1: return [s]
    answer = [s//n for _ in range(n)]
    rest = s%n
    for i in range(1, rest+1):
        answer[-i] += 1
    return answer
