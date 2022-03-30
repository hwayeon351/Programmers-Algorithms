from collections import deque
import string

tmp = string.digits + string.ascii_uppercase

def convert_10_to_n(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert_10_to_n(q, base) + tmp[r]

def solution(n, t, m, p):
    answer = ''
    num = 0
    turn = 1
    while len(answer) < t:
        q = deque(convert_10_to_n(num, n))
        while q:
            c = q.popleft()
            if turn == p:
                answer += c
                if len(answer) == t: break
            turn += 1
            if turn > m: turn = 1
        num += 1

    return answer
