def solution(n, left, right):
    answer = []
    for i in range(int(left), int(right)+1):
        row = int(i) // n + 1
        col = int(i) % n + 1
        answer.append(max(row, col))

    return answer
