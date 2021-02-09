def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):  
        answer.append(bin(a1 | a2)[2:].rjust(n, "0").replace("1", "#").replace("0"," "))
    return answer
