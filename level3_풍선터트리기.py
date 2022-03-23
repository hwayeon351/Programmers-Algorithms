def solution(a):
    min_left, min_right = 1000000001, 1000000001
    check = [0]*len(a)
    for i in range(len(a)):
        if a[i] < min_left:
            min_left = a[i]
            check[i] = 1
        if a[-1-i] < min_right:
            min_right = a[-1-i]
            check[-1-i] = 1
    
    return sum(check)
