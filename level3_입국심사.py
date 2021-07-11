def solution(n, times):
    answer = 0
    left = 1
    right = min(times)*n
    while left <= right:
        mid = (left+right)//2
        cnt = 0
        for t in times:
            cnt += mid//t
            if cnt >= n:
                answer = mid
                right = mid-1
                break
        if cnt < n:
            left = mid+1        
    return answer
