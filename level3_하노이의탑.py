def hanoi(num, _from, by, to):
    global answer
    if num == 1: 
        answer.append([_from, to])
        return
    hanoi(num-1, _from, to, by)
    answer.append([_from, to])
    hanoi(num-1, by, _from, to)
        
def solution(n):
    global answer
    answer = []
    hanoi(n, 1, 2, 3)
    return answer
