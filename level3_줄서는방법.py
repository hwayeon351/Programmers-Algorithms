from math import factorial
def solution(n, k):
    answer = []
    people = [p for p in range(1, n+1)]
    while people:
        fac = factorial(n-1)
        q, r = divmod(k, fac)
        if r == 0: q -= 1
        answer.append(people.pop(q))
        k = r
        n -= 1
    return answer
