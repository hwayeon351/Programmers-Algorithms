def solution(board, skill):
    answer = 0
    skills = [[0] * (len(board[0])+1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            skills[r1][c1] -= d
            skills[r1][c2 + 1] += d
            skills[r2 + 1][c1] += d
            skills[r2+1][c2 + 1] -= d
        else:
            skills[r1][c1] += d
            skills[r1][c2 + 1] -= d
            skills[r2 + 1][c1] -= d
            skills[r2 + 1][c2 + 1] += d

    for c in range(len(board[0])+1):
        n_sum = 0
        for r in range(len(board)+1):
            skills[r][c] += n_sum
            n_sum = skills[r][c]

    for r in range(len(board)+1):
        n_sum = 0
        for c in range(len(board[0])+1):
            skills[r][c] += n_sum
            n_sum = skills[r][c]


    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] + skills[r][c] > 0: answer += 1

    return answer
