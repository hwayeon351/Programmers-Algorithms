import heapq

def solution(rows, columns, queries):
    answer = []
    arr = [[0]*(columns+1) for _ in range(rows+1)]
    
    num = 1
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            arr[i][j] = num
            num += 1

    for r1, c1, r2, c2 in queries:
        nums = []
        temp = arr[r1][c1]
        
        #(r2, c1) -> (r1, c1)
        for r in range(r1, r2):
            arr[r][c1] = arr[r+1][c1]
            heapq.heappush(nums, arr[r+1][c1])
            
        #(r2, c2) -> (r2, c1)
        for c in range(c1, c2):
            arr[r2][c] = arr[r2][c+1]
            heapq.heappush(nums, arr[r2][c+1])
            
        #(r1, c2) -> (r2, c2)
        for r in range(r2, r1, -1):
            arr[r][c2] = arr[r-1][c2]
            heapq.heappush(nums, arr[r-1][c2])
            
        #(r1, c1) -> (r1, c2)
        for c in range(c2, c1+1, -1):
            arr[r1][c] = arr[r1][c-1]
            heapq.heappush(nums, arr[r1][c-1])
        arr[r1][c1+1] = temp
        heapq.heappush(nums, temp)
        
        answer.append(heapq.heappop(nums))   
    
    return answer
