def solution(numbers, hand):
    keypad = {1:['L', [0, 0]], 4:['L', [0, 1]], 7:['L', [0, 2]], 3:['R', [2, 0]], 6:['R', [2, 1]], 9:['R', [2, 2]], 2:['LR', [1, 0]], 5:['LR', [1, 1]], 8:['LR', [1, 2]], 0:['LR', [1, 3]]}
    left = [0, 3]
    right = [2, 3]
    answer = ''
    for n in numbers:
        if keypad[n][0] == 'L':
            answer += keypad[n][0]
            left = keypad[n][1]
        elif keypad[n][0] == 'R':
            answer += keypad[n][0]
            right = keypad[n][1]
        else:
            l_dis = abs(left[0]-keypad[n][1][0]) + abs(left[1]-keypad[n][1][1])
            r_dis = abs(right[0]-keypad[n][1][0]) + abs(right[1]-keypad[n][1][1])
            if l_dis == r_dis:
                if hand == 'right':
                    answer += 'R'
                    right = keypad[n][1]
                else:
                    answer += 'L'
                    left = keypad[n][1]
            elif l_dis < r_dis:
                answer += 'L'
                left = keypad[n][1]
            else:
                answer += 'R'
                right = keypad[n][1]
    return answer
