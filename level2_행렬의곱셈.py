def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for row in range(len(arr1))]
    for row in range(len(arr1)):
        for col in range(len(arr2[0])):
            sum = 0
            for i in range(len(arr1[0])):
                sum += (arr1[row][i] * arr2[i][col])
            answer[row][col] = sum
    return answer
