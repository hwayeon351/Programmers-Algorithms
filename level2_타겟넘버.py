answer = 0
def dfs(i, n_sum, numbers, target):
    global answer
    if i == len(numbers):
        if n_sum == target:
            answer += 1
        return
    dfs(i+1, n_sum+numbers[i], numbers, target)
    dfs(i+1, n_sum-numbers[i], numbers, target)

def solution(numbers, target):
    dfs(0, 0, numbers, target)
    return answer
