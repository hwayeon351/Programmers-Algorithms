def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    while left <= right:
        mid = (left+right)//2
        blank = 0
        for s in stones:
            if s < mid:
                blank += 1
            else:
                blank = 0
            if blank == k:
                break
        if blank < k:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1
    return answer
