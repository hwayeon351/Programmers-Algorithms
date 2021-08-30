def solution(board, moves):
    answer = 0
    stack = []
    for m in moves:
        for row in range(len(board)):
            if board[row][m-1] != 0:
                if len(stack) > 0:
                    if stack[-1] == board[row][m-1]:
                        answer += 2
                        stack.pop()
                    else: stack.append(board[row][m-1])
                else: stack.append(board[row][m-1])
                board[row][m-1] = 0
                break
    return answer
